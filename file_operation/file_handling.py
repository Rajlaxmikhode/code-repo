with open("hello.txt","r") as f:
    for line_number,line in enumerate(f):
        print(f'{line_number+1}:  {line}')
    