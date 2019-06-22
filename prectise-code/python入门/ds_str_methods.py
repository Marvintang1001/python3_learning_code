name='marvin_tang'

if name.startswith('marvin'):
    print('Yes, the string starts with "marvin"')

if name.find('tang') != -1:
    print('Yes,it contains the string "tang"')

delimiter = '_*_'
mylist=['China','Russia','India','Japan']
print(delimiter.join(mylist))
