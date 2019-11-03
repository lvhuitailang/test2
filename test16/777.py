class Test():
    def __add__(self, other):
        print('调用了__add__方法，')

    def __iadd__(self, other):
        print('调用了__iadd__方法')



if '__main__' == __name__:
    a = Test()
    a = a+1
    print('=================')
    a = Test()
    a += 1
