import math
import mmh3


class BloomFilter:

    # To create bit array of size n
    '''
      size - size of bit array calc based the formula
      k    - no. of hash function used to hash the value
      p    - probability of false positive
    '''

    def __init__(self, n):
        self.p = 0.05
        self.size = math.ceil(-n*math.log(self.p)/(math.log(2)**2))
        self.k = math.ceil(self.size/n*math.log(2))
        self.bit_array = [0] * self.size
        self.validate_array = []

    # Func to insert values into BF
    def insert(self, value, freq=1):
        line_hash = str(mmh3.hash(value,freq))
        for i in range(self.k):
            index = mmh3.hash(line_hash,i) % self.size
            self.bit_array[index] = 1

    # To check if the value is present in BF or not
    def validate(self, value, freq=1):
        line_hash = str(mmh3.hash(value,freq))
        for i in range(self.k):
            check_at_index = mmh3.hash(line_hash,i) % self.size
            if self.validate_array[check_at_index] == 1:
                continue
            else:
                return False
        return True

    def readBloomFilterFromFile(self,filename):
        f = open(filename, "rb")
        self.validate_array = list(f.read())
        for i in range(0, len(self.validate_array)):
            self.validate_array[i] -= 48
        print(self.validate_array)
        f.close()
    
    def readBloomFilterFromBytes(self,bf_as_bytes):
        self.validate_array = list(bf_as_bytes)
        for i in range(0, len(self.validate_array)):
            self.validate_array[i] -= 48
        print(self.validate_array)
    
    # Returns the bit array
    def getBloomFilter(self):
        return self.bit_array

    # Returns the size of the bit arry
    def getSize(self):
        return self.size

    def getNFromSize(self,size):
        return(math.floor(size*-1*(math.log(2)**2)/math.log(self.p)))

    # Returns the # of Hash Functions ie. h1(k), h2(k) ...
    def getNumberOfHashFunctions(self):
        return self.k

    def getAsBytes(self):
        return str.encode(''.join([str(i) for i in self.bit_array]))
