

class MyList():

    def __init__(self,lst):
        self.lst = lst

    def __str__(self):
        returnStr = '['
        for x in self.lst:
            returnStr += str(x)
            returnStr += ','
        returnStr = returnStr[:-1]
        returnStr += ']'
        return returnStr

    def __mul__(self, other):
        listTemp = []
        for x in range(len(self.lst)):
            listTemp.append(self.lst[x]*other)
        return MyList(listTemp)

    def __rmul__(self, other):
        listTemp = []
        for x in range(len(self.lst)):
            listTemp.append(self.lst[x]*other)
        return MyList(listTemp)


if '__main__' == __name__:
    a = MyList([1,2,3])
    print('原始数据:',end='')
    print(a)
    print(a*3*2*4*9)# 正向运算符
    print(3*a)# 逆向运算符
    print((3*a).lst)# 正向 返回list类型(逆向运算符计算同理)