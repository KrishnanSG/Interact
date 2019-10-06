from BloomFilter import BloomFilter
import sys

# Get filename for sync
try:
    filename = sys.argv[1]
except IndexError:
    print("No file staged for synchronization")
    sys.exit()




def sendBloomFilter():

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

def readBloomFilter(n):
    receivedBF = BloomFilter(n)
    receivedBF.readBloomFilterFromFile()
    user_file_content ={}
    with open(filename) as user_file:
        for line in user_file:
            try:
                user_file_content[line]+=1
            except:
                user_file_content[line]=1
            if not receivedBF.validate(line):
                print(line,end='')

#sendBloomFilter()
readBloomFilter(5)