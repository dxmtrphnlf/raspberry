import RPi.GPIO as GPIO
from abc import ABCMeta


class BaseSensor(metaclass=ABCMeta):
    """
    Abstract class for all sensors
    """
    gpio = GPIO

    def __init__(self, pin: int):
        assert pin > 0, 'Pin must be positive int value'
        self.pin = pin


class InputSensor(BaseSensor, metaclass=ABCMeta):
    """
    Abstract class for sensors that accept information
    """

    def __init__(self, pin: int):
        super(InputSensor, self).__init__(pin)
        self.gpio.setup(pin, GPIO.IN)


class OutputSensor(BaseSensor, metaclass=ABCMeta):
    """
    Abstract class for sensors that display information
    """

    def __init__(self, pin: int):
        super(OutputSensor, self).__init__(pin)
        self.gpio.setup(pin, GPIO.OUT)

    def __del__(self):
        self.gpio.output(self.pin, GPIO.LOW)
        self.gpio.setup(self.pin, GPIO.LOW)
