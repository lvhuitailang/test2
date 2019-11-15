import re

regx_ = re.compile(r'(aa)(b)',re.I)

res = re.search(regx_,'aabbb')

print(res.lastindex)