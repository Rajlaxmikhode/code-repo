#The process of transforminng string into series of bytecode is calles as encoding .
print("eg.1")
string="Python"
tobytecode=string.encode('UTF-8')
print("encode:",tobytecode)

#The process of transforming byte code to sstring is decoding it's vice versa of encoding.
string=tobytecode.decode('utf-8')
print("decode:",string)
print("---------------------------")
#eg.2
print("eg.2")
name="Manvi"
tobytecode=name.encode('utf-8')
print("encode:",tobytecode)
name=tobytecode.decode('utf-8')
print("decode:",name)