with open("sample.txt","w")as file:
    bytes_written=file.write("Old is Gold!")
    print(bytes_written)

with open("sample.txt","r") as file:

    file.seek(5)#move pointer to index 5

    text_read=file.read(4)#read 4 characters
    print(text_read)

    current_pos=file.tell()#get current position
    print(current_pos)
    
    