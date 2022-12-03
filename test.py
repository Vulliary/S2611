# class Student:
#     print('Hi')
# st1 = Student()
# st2 = Student()
# st3 = Student()

class Student:
    education = "Step"

    def __init__(self):
        self.name = 'Oleg'
        self.age = 15
        self.height = 156
        print("Все получилось♥")
        # print(id(self))


st1 = Student()
print(st1.education)
print(st1.name)
print(st1.age)
print(st1.height)
st2 = Student()
