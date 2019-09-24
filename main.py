from BloomFilter import BloomFilter

# Note to be implemented  using Command line arguments

filename = "BloomFilter.py"
user_file_content = []


with open(filename) as user_file:

    for line in user_file:
        user_file_content.append(line)

user_file_NOL = len(user_file_content)

bloom_filter = BloomFilter(user_file_NOL)

for blocks in user_file_content:
    bloom_filter.insert(blocks)

print(bloom_filter.getBloomFilter())
print(bloom_filter.getSize())
print(bloom_filter.getNumberOfHashFunctions())

print(user_file_content[1])
print(bloom_filter.validate(user_file_content[1]))


with open("test", "wb") as f:
    for i in bloom_filter.getBloomFilter():
        if i == 0:
            f.write(b"0")
        else:
            f.write(b"1")
