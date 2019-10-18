class Mylist():
    def __init__(self,a):
        self.a=a
        self.count=0
    def __str__(self):
        return self.a
    def __mul__(self, other):
        for x in self.a:
            self.a[self.count]=x * other
            self.count+=1
        return self.a
    def __rmul__(self, other):
        for x in self.a:
            self.a[self.count]=x * other
            self.count+=1
        return self.a

a=Mylist([1,2,3,4])
print (3*a)