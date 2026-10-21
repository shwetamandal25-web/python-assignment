class Car:

    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print(self.speed)

    def brake(self, amount):
        self.speed = self.speed - amount

        if self.speed < 0:
            self.speed = 0

        print(self.speed)


car = Car("BMW")

car.accelerate(20)
car.accelerate(30)

car.brake(10)
car.brake(50)