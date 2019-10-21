import mmh3
def syncFile(filename,my_missing_content,received_missing_content):
    
    file_content=[]
    lines_to_insert=[]

    # Read file
    with open(filename,'r') as f:
        file_content=f.readlines()

    for i in received_missing_content:
        
        if i in my_missing_content:
            # Present so update contents
            file_content[i-1]=received_missing_content[i]
            del(my_missing_content[i])
        else:
            # Not Present so insert no line
            lines_to_insert.append(i)

    # Line insertion
    for i in lines_to_insert:
        file_content.insert(i-1,received_missing_content[i])
    
    # Line deletion
    for i in my_missing_content.keys():
        file_content.pop(i-1)

    # Write into file
    with open(filename,'w') as f:
        f.writelines(file_content)

def computeHash(filename):
    # returns 4 byte hash value of the file
    file_reader = open(filename,"rb")
    file_contents = file_reader.read()
    n=abs(mmh3.hash(file_contents)) % 2**32
    return (n.to_bytes((n.bit_length()+7)//8,'big'))

