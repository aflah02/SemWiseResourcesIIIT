
# class Student:
#     cs = 0
#     c = 0
#     def __init__(self, roll, cost):
#         self.roll = roll
#         Student.cs += 1
#         Student.c += Student.cost

# class Professor:
#     cp = 0
#     x = 0
#     def __init__(self,id, cost):
#         self.id = id
#         Professor.cp += 1
#         Professor.c += Professor.cost

# x = int(input('s cost'))
# y = int(input('p cost'))

# Student.cost = x
# Professor.cost = y

# s1 = Student(10,x)
# print(Student.cost)

class qua:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def changea(self, a):
        self.a = a
    def changea(self, b):
        self.b = b   
    def changea(self, c):
        self.c = c
    def pri(self):
        return(f'{self.a}x^2 + {self.b}x^2 + {self.c}')
    def y(self, object):
        x = self.a + object.a
        y = self.b + object.b
        z = self.c + object.c
        w = qua(x,y,z)
        return w

x = qua(2,3,4)
z = qua(6,4,1)
c = x.y(z)
print(c.pri())