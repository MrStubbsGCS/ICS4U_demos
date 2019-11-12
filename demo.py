class Vehicle:
    def __init__(self, capacity, speed):
        self.capacity = capacity
        self.speed = speed


class SpaceShip(Vehicle):
    def __init__(self, numberOfRockets, inSpace, capacity, speed):
        super().__init__(capacity, speed)
        self.numberOfRockets = numberOfRockets
        self.inSpace = inSpace

class MilleniumFalcon(SpaceShip):
    def __init__(self, guns, chewbaccas, numberOfRockets, inSpace, capacity, speed):
        super().__init__(numberOfRockets, inSpace, capacity, speed)
        self.guns = guns
        self.chewbaccas = chewbaccas

    def isHanDed(self):
        return True


falconX = SpaceShip(4, False, 0, 300)
milFalc = MilleniumFalcon(4, 1, 10, True, 100, 6)
print(milFalc.isHanDed())