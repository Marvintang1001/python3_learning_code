#for i in range(1,5):
#    print(i)

while True:
    s=input('Enter something: ')
    if(s=='quit'):
        break
    if s.find("bad") != -1:
        if s.find("wife")!= -1:
            print("It is impossible!! again")
            continue
    else:
        print('Well done!')
print('done')
