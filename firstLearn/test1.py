import random
'''
a = random.choice(range(100))
b = random.choice(range(100))
print('a: ',a,' b: ',b)
if (a > b):
    print('a > b')
elif (a == b):
    print('a == b')
else:
    print('a < b')
'''

'''
sites = ['baidu','google','sina','yahoo','jd']
for site in sites:
    if(site == 'sina'):
        print('break site: ',site)
        break
    print('loop ...',site)
else:
    print('no site')
print('end loop')

'''
# a = [8,5,4,9,2]
# for i,j in enumerate(a):
#     print(i,' ',j)

a = 'acb'
b = list(a)
b.sort()
print(b)
