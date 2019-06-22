class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):     #告诉我细节信息
        print('Name: {} Age: {}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: ',self.salary)

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student: {} ）'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: ',self.marks)

t=Teacher('Mrs.XU',24,10000)
s=Student('Marvin',25,100)

print()
members=[t,s]
for member in members:
    member.tell()


