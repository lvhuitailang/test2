
items = ['a','b','c','d']
items = [x for i,x in enumerate(items) if i<len(items)-1 ]
print(items)