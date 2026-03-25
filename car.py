class Car:
    def __init__(self, initial_speed):
        self._speed = initial_speed

    def accelerate(self):
        self._speed += 1

    def brake(self):
        self._speed -= 1

    @property
    def speed(self):
        return self._speed
