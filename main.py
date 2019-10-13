import argparse
import os
import sys
import time
from math import floor,log

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from BloomFilter import BloomFilter
from P2P.Server import NetworkManager

# Create the parser
my_parser = argparse.ArgumentParser(description='Sync two files')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the file path to sync')


my_parser.add_argument('Role',
                       metavar='role',
                       type=int,
                       help='1  - if host, 0 - client')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path
input_path = os.path.abspath(input_path)
role = args.Role

p2p = NetworkManager()

if not os.path.isfile(input_path):
    print('\n',input_path, '- Not a valid file to stage for syncing')
    sys.exit()

def on_modified(event):
    if os.path.abspath(event.src_path) == input_path:
        # Detect changes from only the given path.
        # Ignore all other changes
        print(f"Detected changes {event.src_path} has been modified")
        print("Redrawing the bloom filter ...")
        print("Sending the bloom filter ...")
        bf = sendBloomFilter()
        p2p.send_data(bf.getAsBytes(), NetworkManager.REQUEST_BLOOMFILTER)


class FileEventHandler(PatternMatchingEventHandler):
    def __init__(self, patterns=None, ignore_patterns=None, ignore_directories=False, case_sensitive=False,
                    on_modified_callback=on_modified):
        self.on_modified_callback  = on_modified_callback
        self.last_modified = time.time()
        return super().__init__(patterns=patterns, ignore_patterns=ignore_patterns,
                            ignore_directories=ignore_directories, case_sensitive=case_sensitive)
        
    def on_modified(self, event):
        if(time.time() - self.last_modified) > 1:
            self.on_modified_callback(event)
            self.last_modified = time.time()
        return super().on_modified(event)

# Use this func to find n required for BloomFilter
# Size is the len of bloomfilter bit array
def getNFromSize(size):
    return(floor(size*-1*(log(2)**2)/log(0.05)))

def main():
    print("Starting server...")
    print("Watching", input_path, "for changes...")
    patterns = "*"
    ignore_patterns = ["*.save"]
    ignore_directories = True
    case_sensitive = True
    file_event_handler = FileEventHandler(patterns, ignore_patterns, ignore_directories,
                                case_sensitive, on_modified_callback=on_modified)

    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(file_event_handler, path, recursive=go_recursively)
    
    my_observer.start()


    if role==1:
        p2p.create_host()
    else:
        ip = input("Enter an IP: ")
        #ip = '127.0.1.1' 
        port = int(input("Enter a PORT: "))
        p2p.create_client(ip,port)


    try:
        while True:
            a = p2p.check_if_incoming_data()
            
            request_type, request_data = a[0], a[1]
            # print(request_type, request_data)
            # print(p2p.check_if_incoming_data())
            if(request_type == NetworkManager.REQUEST_BLOOMFILTER):
                # The opposite party has sent its bloom filter and now requesting ours
                # We send it now
                print("Received the bloom filter, acknowleding and transmitting the bloom filter")
                bf = sendBloomFilter()
                p2p.send_data(bf.getAsBytes(), NetworkManager.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER)
                print("---------BF from user2--------------")
                
                # Example
                # bf_bytes = request_data[:-4]
                # missing_content = getMissingContent(getNFromSize(len(bf_bytes)),bf_bytes)
                # follow next step refer P2P/READEME.md 

            elif(request_type == NetworkManager.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER):
                
                print("Request was acknowledged by the other peer and has given the other bloom filter")
                print("---------BF from user2--------------")
                print(request_data[:-4])
                
                # Example
                # bf_bytes = request_data[:-4]
                # missing_content = getMissingContent(getNFromSize(len(bf_bytes)),bf_bytes)
                # follow next step refer P2P/READEME.md
                
                ## TODO: Do whatever to be done when we have given the original request and got the other bloom filter

            
            # p2p.check_pending_outgoing()
            # p2p.send_data("sadasdasdasdffd")
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

def sendBloomFilter():
    filename = input_path

    # total # of line in the file
    user_file_NOL = 0

    # content frequency
    user_file_content = {}

    with open(filename) as user_file:
        for line in user_file:
            user_file_NOL += 1
    # creates bloomfilter of required size
    bloom_filter = BloomFilter(user_file_NOL)

    # read contents of file and insert into BF
    with open(filename) as user_file:
        for line in user_file:
            try:
                user_file_content[line]+=1
            except:
                user_file_content[line]=1
            bloom_filter.insert(line,freq=user_file_content[line])
    # create output file for BF transmission
    with open("bloomfilter.bin", "wb") as f:
        for i in bloom_filter.getBloomFilter():
            if i == 0:
                f.write(b"0")
            else:
                f.write(b"1")

    return bloom_filter


def getMissingContent(n,bloomfilter_bytes):
    missing_content={}
    receivedBF = BloomFilter(n)
    receivedBF.readBloomFilterFromBytes(bloomfilter_bytes)
    user_file_content ={}
    line_number=0
    with open(input_path) as user_file:
        for line in user_file:
            line_number+=1
            try:
                user_file_content[line]+=1
            except:
                user_file_content[line]=1
            if not receivedBF.validate(line):
                missing_content[line_number]=line
                return(missing_content)


if __name__ == "__main__":
    
    main()
