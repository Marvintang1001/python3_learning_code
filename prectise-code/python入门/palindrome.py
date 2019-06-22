def reverse(text):
    return text[::-1]

def palindrome(text):
    return text==reverse(text)

something=input("Text: ")
tx=tuple(something)
forbidden=['!','.','/','?',',',' ']

txlist=[]

for character in tx:
    print(character)
    if character not in forbidden:
         txlist+=character

mytx="".join(txlist)
print(mytx)

if palindrome(mytx):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')


