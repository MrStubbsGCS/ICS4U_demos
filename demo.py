class WaterBottle:
    def __init__(self, volume, colour, shape):
        self.volume = volume
        self.colour = colour
        self.shape = shape

    def __len__(self):
        return self.volume


    def __str__(self):
        return "Our water bottle is a " +self.colour+self.shape

camelback = WaterBottle(500, "Orangey pinkish red or maybve coral idk", "cylinder")

print(len(camelback))