
class ShortInputException(Exception):   #自定义一个异常
    def __init__(self,length,atleast):  #获取输入文本长度length，期望最小长度atleast
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    text=input('Enter something --> ')
    if len(text)<3:
        raise ShortInputException(len(text),3)

except EOFError:
    print('It is a EOF error.')
except ShortInputException as ex:       #将该类存储 as（为） 相应的错误名或异常名。这类似于函数调用中的形参与实参。
    print(('ShotInputException: The input was '+'{0} long,expected at least {1}').format(ex.length,ex.atleast))
else:
    print('No exception was raised.')
