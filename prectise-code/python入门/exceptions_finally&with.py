import sys,time

f=None
try:
#    f=open('baby.txt')
    with open('baby.txt')as f:
        while True:
        #line=f.readline()
            for line in f:
                if len(line)==0:
                    break
                print(line,end='')
                sys.stdout.flush()
                print('Press ctrl+c now')
                time.sleep(3)
except IOError:
    print('Could not find file baby.txt')
except KeyboardInterrupt:
     print('You cancelled the reading file')
finally:
#    if f:
 #       f.close()
    print('(cleaning up: Closed the file)')
