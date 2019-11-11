import mmh3
def syncFile(filename,my_missing_content,received_missing_content):
    
    file_content=[]
    contents_to_modify=[]

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
            # lines_to_insert.append(i)
            contents_to_modify.append([i,'i',received_missing_content[i]])

    for i in my_missing_content.keys():
        contents_to_modify.append([i,'d'])
    contents_to_modify.sort()

    def update_lines(flag):
        for i in range(len(contents_to_modify)):
            if contents_to_modify[i][1]=='d':
                contents_to_modify[i][0]+=flag
        
        
    while contents_to_modify:
        i=contents_to_modify.pop(0)
        # Insert
        if i[1]=='i':
            file_content.insert(i[0]-1,i[2])
            update_lines(1)
        # Delete
        else:
            file_content.pop(i[0]-1)
            update_lines(-1)

    # Write into file
    with open(filename,'w') as f:
        f.writelines(file_content)

def computeHash(filename):
    # returns 4 byte hash value of the file
    file_reader = open(filename,"rb")
    file_contents = file_reader.read()
    n=abs(mmh3.hash(file_contents))
    return (n.to_bytes((n.bit_length()+7)//8,'big'))