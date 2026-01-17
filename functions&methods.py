#A function is a set of instruction used to perform some particular operations.Like print(),input(),len() etc...
#When a funnction belong  to  specific to kind of objects and something is called method it is accessed usig  dot  operator.Eg:replace(),upper(),find() ,etc
Course="Python course  for Beginners"
print(len(Course))
print(Course.upper()) #This doesn't modify the  existing  string ,it returns  a new string
print(Course.replace("Python","Py"))
print(Course.find("Python")) #return the  lowest index of the string
print("for"  in Course) #returns a  booloean value
print("python" in Course)
print(Course.lower())
