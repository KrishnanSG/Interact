from BloomFilter import BloomFilter
import sys

# Get filename for sync
try:
    filename = sys.argv[1]
except IndexError:
    print("No file staged for synchronization")
    sys.exit()

def createBloomFilter():

    # read contents of file
    user_file_content = []
    with open(filename) as user_file:
        for line in user_file:
            user_file_content.append(line)

    # total # of line in the file
    user_file_NOL = len(user_file_content)

    # creates bloomfilter of required size
    bloom_filter = BloomFilter(user_file_NOL)   

    # insert into BF
    for blocks in user_file_content:
        bloom_filter.insert(blocks)

    # create output file for BF transmission 
    with open("bloomfilter.bin", "wb") as f:
        for i in bloom_filter.getBloomFilter():
            if i == 0:
                f.write(b"0")
            else:
                f.write(b"1")
