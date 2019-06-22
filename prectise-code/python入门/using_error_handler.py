try:
    text=input('Enter: ')
except EOFError:
    print('It is a EOF error')
except KeyboardInterrupt:
    print('It is a keyboardInterrupt')
else:
    print('successful:',text)
