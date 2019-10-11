my_missing_content={3:'3\n',4:'4\n',6:'6'}
received_missing_content={1:'7\n',3:'20\n',4:'42\n'}

file_content=[]
lines_to_insert=[]

with open('file3','r') as f:
    file_content=f.readlines()
print(file_content)

for i in received_missing_content:
    
    if i in my_missing_content:
        # Present so update contents
        file_content[i-1]=received_missing_content[i]
        print("Line ",i," updated with content ",received_missing_content[i])
        del(my_missing_content[i])
    else:
        # Not Present so insert no line
        # file_content.insert(i-1,received_missing_content)
        lines_to_insert.append(i)
        print("Line ",i," inserted with content ",received_missing_content[i])
    # my_missing_content[i]=received_missing_content[i]
    # print("Line ",i," updated with content ",my_missing_content[i])

for i in lines_to_insert:
    file_content.insert(i-1,received_missing_content[i])
print(my_missing_content)
for i in my_missing_content.values():
    file_content.remove(i)
print(file_content)

with open('file3','w') as f:
    f.writelines(file_content)
    