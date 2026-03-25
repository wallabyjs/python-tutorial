from car import Car

class TestCar:
    def test_initial_speed(self):
        car = Car(88)
        # Wallaby captures print() output and displays it inline
        print(f"Initial speed: {car.speed}")
        assert car.speed == 88

    def test_accelerate(self):
        car = Car(88)
        # Uncomment the lines below to see code coverage update in real-time
        # car.accelerate()
        # assert car.speed == 89

    def test_brake(self):
        car = Car(88)
        # car.brake()
        # assert car.speed == 87
