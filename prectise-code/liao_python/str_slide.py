def trim(s):
    if s[:1]==' ':
        return trim(s[1:])
    if s[-1:]==' ':
        return  trim(s[:-1])
    return s

#print(trim(''))


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败a!')
elif trim('  hello') != 'hello':
    print('测试失败b!')
elif trim('  hello  ') != 'hello':
    print('测试失败c!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败d!')
elif trim('') != '':
    print('测试失败e!')
elif trim('    ') != '':
    print('测试失败f!')
else:
    print('测试成功!')

