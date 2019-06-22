#print("Hello World")
#help(int())
length = 5
breadth=2
area= length * breadth
#print('Area is', area)
#print('Perimeter is',2*(breadth*length))

a=1
running=True
while running:
    guess=int(input('Enter an integer : '))
    if guess == length:
        print('Congratulatons, you guessd it. but you do not win any prizes!')
        running= False
    elif guess < length :
        print('no, it is little higher than that')
    else:
        print('no,it is little lower than that')
else:
    a+=1
    print(a)
print('done')


