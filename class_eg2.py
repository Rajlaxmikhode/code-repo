class Point: 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        sum=x+y
        print("sum of two digits is: ",sum)
        
    def sub(self,x,y):
        sub=x-y
        print("difference of two digits is: ",sub)
        return sub

obj=Point(7,9)
obj1=Point(17,9)
obj.sub(13,7)
obj1.sub(13,9)


   
