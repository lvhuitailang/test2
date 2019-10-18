import random
'''
    人类
    sex:男   女
    type:大人 小孩
    toString:字符串输出结果

'''
class Person():
    sex = '男'
    type = '大人'
    toString = '(男,大人)'

    def __init__(self,sex,type):
        if sex is None or type is None:
            self.toString = '计算错误'
            return
        self.sex = sex
        self.type = type
        self.toString = '('+sex+','+type+')'

    def __str__(self):
        return self.toString

    def __add__(self, other):
        if self.sex != other.sex and self.type =='大人' and other.type == '大人':
            return Person(random.choice(['男','女']),'小孩')
        else:
            return Person(None,None)


if '__main__' == __name__:
    p1 = Person('男','大人')
    p2 = Person('女','大人')
    print(p1+p2)


