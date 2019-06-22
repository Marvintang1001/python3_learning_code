import threading

#多线程：
#max_count=100  线程数
#args- 传递给线程函数的参数,他必须是个tuple类型
#kwargs - 可选参数
#start():启动线程活动。
#join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
#__init__ 用于定义实例属性
#self.getName()   获取线程名字
from django.db.models import F

from weibo.models import WeiboUser

# 直接从Thread继承，创建一个新的class，把线程执行的代码放到这个新的 class里
class ChangeThread(threading.Thread):
    #改变用户状态:

    def __init__(self, max_count=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self):
        count = 0
        user = WeiboUser.objects.get(pk=6)
        while True:
            #最多循环max_count:
            if count >= self.max_count:
                break

            print(self.getName(), count)
            #10 11 SET status =11
            #user.status += 1

            #每次修改前先查数据库，从数据库层面修改
            #set status = status +1
            user.status = F('status') + 1
            user.save()
            count += 1

def main():
    t1 = ChangeThread(max_count=800)
    t2 = ChangeThread(max_count=500)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


