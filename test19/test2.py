import re
def doit():
    exp = input('input a expression:\n')
    #假设式子格式正确
    result = extract(exp)



'''
1*(2+3)-4+5*(6-7)
'''
def extract(exp):
    bracket_re = re.compile(r'(\(.*?\))')
    result = bracket_re.findall(exp)
    for x in result:
        aaa = dealStraightline(x)
        pass

    pass

def dealStraightline(exp):
    if re.search(r'(\(.*?\))',exp):
        reg = re.compile(r'(\d)([\*\/\+\-])(\d)')
        targetStr = reg.findall(exp)
        replace = calc(targetStr[0][0],targetStr[0][1],targetStr[0][2])
        exp =re.sub(reg,replace,exp,1)
        print(exp)
        pass
    else:
        return exp

#计算
def calc(num1,op,num2):
    if '*' == op:
        return int(num1)*int(num2)
    elif '/' == op:
        return int(num1)/int(num2)
    elif '+' == op:
        return int(num1)+int(num2)
    elif '-' == op:
        return int(num1)-int(num2)




if __name__ == '__main__':
    doit()