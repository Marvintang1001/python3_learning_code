myset=set(['apple','banana','apple'])
for fruit in myset:
    print(fruit, end=' ')

myset2=myset.copy()
myset2.add('orange')
print('\n',myset2.issuperset(myset))

for fruit in myset2:
    print(fruit, end=' ')

myset2.remove('orange')
print('\n'+str(myset2 & myset))
