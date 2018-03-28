class Myclass1(object):
    def __init__(self,maxsize):
        self.maxsize= maxsize
        self.listval=[]
    def push_val(self,x):
        self.listval.append(x)
        if len(self.listval)>self.maxsize:
            print ("Value cannot be added as it exceeds the length")
            self.listval.pop(0)
    def get_val(self):
        return self.listval


a= Myclass1(3)
b= Myclass1(3)
b=Myclass1("1")
a.push_val("Hi")
a.push_val("Hello")
a.push_val("bye")
a.push_val("4")

print a.get_val()

