import time
#cock  a=>5yuan  (a=range(0,21))
#hen  b=>3yuan   (b=range(0,34))
#chick   c=>0.5yuan   (c=range(0,201))

#my algorism:
#start=time.clock()
start=time.perf_counter()
for a in range(0,21):
    for b in range(0,34):
        for c in range(0,201):
            if 5*a+3*b+0.5*c==100 and a+b+c==100:
                print(a,b,c)
#end=time.clock()
end=time.perf_counter()
time1=end-start
print('time1=',time1)

