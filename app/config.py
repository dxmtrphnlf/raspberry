import RPi.GPIO as GPIO


class AppConfig:

    def __init__(self, sensors: list):
        self.sensors = sensors
        self._setup()

    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        for s in self.sensors:
            s.setup()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for s in self.sensors:
            s.destroy()
        GPIO.cleanup()
