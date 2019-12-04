class Motorcycle(object):
    def __init__(self, maxSpd, spd, sidecar):
        self.sidecar = sidecar
        self.maxSpeed = maxSpd
        self.speed = spd
    def accelerate(self, spd):
        if (self.speed > self.maxSpeed or spd + self.speed > self.maxSpeed):
            print("This motorcycle cannot go that fast.")
        else:
            self.speed = self.speed + spd