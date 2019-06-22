class Robot:
    number=0  #类变量，计数机器人数量

    def __init__(self,name):
        self.name=name
        print('Initializing {}'.format(self.name))
        Robot.number += 1

    def dead(self):
        print('{} is being destroyed!'.format(self.name))
        Robot.number -= 1

        if Robot.number==0:
            print('We have no robot!')
        else:
            print('We still have {:d} robots'.format(Robot.number))

    def say_hi(self):
        print('Hello, my master call me {}'.format(self.name))

    @classmethod
    def baoshu(cls):
        print('The number of our robots is',cls.number)

droid1=Robot('Gandum-00')
droid1.say_hi()
Robot.baoshu()

droid2=Robot('Gandum-Strike_Freedom')
droid2.say_hi()
Robot.baoshu()

print('Gandum-00 is no power!')
droid1.dead()

print('Strike_Freedom have been destroyed!')
droid2.dead()
