############################################----------------------------------------------------------
# Here below I applied encapsulation so it is difficult to modify values outside of class
############################################----------------------------------------------------------

class Cars:
    def __init__(self, speed, color):
        self.__speed = speed             # underscore makes values private to class
        self.__color = color             # underscore makes values private to class

    def set_speed(self, value):
        self.__speed = value             # underscore makes values private to class

    def get_speed(self):
        return self.__speed              # underscore makes values private to class

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

ford = Cars(250, 'Green')
nissan = Cars(300, 'Black')
toyota = Cars(350, 'Blue')

ford.set_speed(500)
ford.speed = 200

toyota.set_color('Orange')
print('toyota is changed to other color',toyota.get_color())

print(ford.get_speed())
#print(ford.__color)