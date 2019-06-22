
def prt(t,q):
    print('{0} --> {1}'.format(t,q))


def hanoi(n,a,b,c):   #a是操作区；b是缓存区；c是目标区。该指令只要看a和c是谁
    if n==1 :
        return prt(a,c)
    hanoi(n-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(n-1,b,a,c)


#hanoi(1)
#hanoi(2)
hanoi(3,'A','B','C')
print('This hanoi tower is end!')
