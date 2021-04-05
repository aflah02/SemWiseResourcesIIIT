class Triangle:
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def checkangles(self):
        if self.angle1 + self.angle2+ self.angle3 == 180:
            return True
        else:
            return False
my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.checkangles())

# class Car:
#     condition = 'new'
#     def __init__(self, color, model, mpg):
#         self.color = color
#         self.model = model
#         self.mpg = mpg
#     def display_car(self):
#         print(f'This is a {self.color} {self.model} with {self.mpg} MPG.')
#     def drive_car(self):
#         Car.condition = 'used'

# class ElectricCar(Car):
#     def __init__(self, color, model, mpg, battery_type):
#         self.battery_type = battery_type
#         Car.__init__(self, color, model, mpg)
#     def drive_car(self):
#         self.condition = 'like new'
# my_car = ElectricCar('Red', 'T10', '10', 'molten_salt')
# print(my_car.condition)
# my_car.drive_car()
# print(my_car.condition)

