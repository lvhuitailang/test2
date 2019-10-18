import re

str = '1+2-3*4/5'
rex = re.compile(r'[\+\-\*\/]')
result = rex.findall(str)

for index,op in enumerate(result):
    print(index)
    str.split()

print(result)
