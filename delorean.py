class DeLorean:
    def __init__(self, engine_volume):
        self.engine = {"type": f"{engine_volume} L"}
        self.body_style = "2-door coupe"
        self.flux_capacitor_shape = "Y"
        self._in_future = False

    def accelerate_to(self, speed):
        if speed == 0:
            self._in_future = True
            return

        if speed > 88:
            self._in_future = True
            return

        return self._in_future

    @property
    def in_future(self):
        return self._in_future
