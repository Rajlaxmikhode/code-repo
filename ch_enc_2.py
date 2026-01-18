var='\u20B9'
print(var)
tobytecode=var.encode('utf-8') #string to byte code i.e unicode to bytecode
print(tobytecode)
var=tobytecode.decode('utf-8') #converts byte code to unicode/string
print(var)

