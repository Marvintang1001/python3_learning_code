my_dict={
    'father':'137xxxxx956',
    'mother':'189xxxxx891',
    'wife':'175xxxxx113',
    'sister':'136xxxxx799'
}

print('my father\'s phone number',my_dict['father'])

del my_dict['sister']    #delect one pair

print('There are {} numbers in my dict'.format(len(my_dict)))   #use format

for name, phone in my_dict.items():
    print('{}=={}'.format(name,phone))     #items: get all pairs

my_dict['brother']='186xxxxx221'

if 'brother' in my_dict:
    print('brother\'s phone is in my_dict which is' ,my_dict['brother'])


