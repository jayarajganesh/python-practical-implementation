class Car:
    def __init__(self, color, model):
        self.color = color  # Assigns the given color to the instance's 'color' attribute
        self.model = model

    def start(self, method1, method2):
        print(self.color)
        print(method1)
        print(method2)

my_car = Car("red", "Tesla")
my_car.start("jay", "raj")
