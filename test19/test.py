import re
def fun(data=None):
    if re.search(r'\s',data) or \
            re.search(r'[a-zA-Z]',data):
        print('你输入的程式不符合规范，请重新输入:')
        fun()
    if re.search(r'[+\-*/]{2,}',data):
        print('你的符号好像出了问题。请重新输入')
        fun()
    if re.search('\([^()]*\)',data):
        ret = fun2(data)
    else:
        fun1 (data)

def fun1(data):
    '''专门处理没有括号的字符'''
    print('专门处理没有括号的字符',data)
    while re.search(r'[+\-*/]',data):
        for i in data:
            if '*' in data or '/' in data:
                if i == '*':
                    cheng = re.search('\d+\*\d+',data).group()
                    rst = int(re.search('\d+',cheng).group()) * int(re.search('(\*)(?P<N>\d+)',cheng).group('N'))
                    data = re.sub(r'(\d+\*\d+)', str(rst), data,1)
                    print(data)
                    break
                elif i == '/':
                    chu = re.search('\d+/\d+',data).group()
                    rst = int(re.search('\d+',chu).group()) / int(re.search('(/)(?P<N>\d+)',chu).group('N'))
                    data = re.sub(r'\d+/\d+', str(int(rst)), data,1)
                    print(data)
                    break
            else:
                if i == '+':
                    jia = re.search('\d+\+\d+', data).group()
                    rst = int(re.search('\d+', jia).group()) + int(re.search('(\+)(?P<N>\d+)', jia).group('N'))
                    data = re.sub(r'\d+\+\d+', str(int(rst)), data,1)
                    print(data)
                    break
                elif i == '-':
                    jian = re.search('\d+-\d+', data).group()
                    rst = int(re.search('\d+', jian).group()) - int(re.search('(-)(?P<N>\d+)', jian).group('N'))
                    data = re.sub(r'\d+-\d+', str(int(rst)), data,1)
                    print(data)
                    break
    return data
def fun2(data):
    '''专门处理有括号的字符'''
    print('专门处理有括号的字符',data)
    bracket = re.findall(r'\([^()]*\)',data)
    bracket = bracket[0]


    bracket = re.split(r'\(|\)',bracket)
    bracket = filter(lambda x:x,bracket)
    bracket = bracket.__next__()
    ret = fun1(bracket)
    data = re.sub(r'\([^()]*\)',ret,data,1)
    print(data)
    fun(data)

def main():
    data = input("请输入你的表达式:").strip()
    fun(data)
if __name__ == '__main__':
    main()