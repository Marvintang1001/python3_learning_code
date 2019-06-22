from python入门.mymodule import tell_my_wife, my_mistake

print('Start:')
#for i in sys.argv:
#    print(i)

#print('\n\nThe PYTHONPATH is', sys.path, '\n')

#print('This code path is',os.getcwd())

if __name__=='__main__':
    print('This program is coding from my hreat:')
else:
    print('I am being imported from another module')

tell_my_wife()
my_mistake()


