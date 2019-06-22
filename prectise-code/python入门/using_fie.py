 #这个斜杠是为了不换行,后面不能有空格
switch='''\
My wife is cuties
When she is idle
if she is happy:
    she like play switch with me

hhhh
'''

f =open('baby.txt','w')
f.write(switch)
f.close()

f=open('baby.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()         #养成close的习惯
