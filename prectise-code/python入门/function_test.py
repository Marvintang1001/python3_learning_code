x=50

def func():
    '''

happy'''
    global x
    print('x is', x)
    x=2
    print('changed local x to', x)

func()
print('x is still',x)


print(func.__doc__)
help(func)
