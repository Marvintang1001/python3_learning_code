#（参数组合）可接收一个或多个数并计算乘积：
def product(*x):
    mul=1
    for i in x:
        mul =mul*i
    return mul

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


#命名关键字参数
'''
def person(name,age,*,city,job='Engineer'):
    print('name',name,'age',age,'other:',city,job)

person('Marvin',25,city='FoShan')
person('Richael',23,city='HuiZhou',job='IT Engineer')
'''

#关键字参数
'''
def person(name,age,**kw):
    print('name',name,'age',age,'other:',kw)

person('Jacky',56)
person('Marvin',25,city='FoShan')
person('Richael',23,city='HuiZhou',job='IT Engineer')
'''

#可变参数
'''
def calc(*num):
    sum=0
    for n in num:
        sum=sum+n*n
    return sum

print(calc(1,3,5,7))
nums=[2,4,6]
print(calc(*nums))
'''

