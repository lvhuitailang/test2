
class MyNumber:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 20:
            self.res = self.num
            self.num += 1
            return self.res
        else:
            raise StopIteration


myClass = MyNumber()
myiter = iter(myClass)

print(next(myClass))
print(next(myClass))
