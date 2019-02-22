import RPi.GPIO as GPIO
from abc import ABCMeta, abstractmethod


class BaseSensor(metaclass=ABCMeta):
    pin = None

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def destroy(self):
        pass


class InputSensor(BaseSensor, metaclass=ABCMeta):
    def setup(self):
        GPIO.setup(self.pin, GPIO.IN)

    def destroy(self):
        pass


class OutputSensor(BaseSensor, metaclass=ABCMeta):
    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)

    def destroy(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.setup(self.pin, GPIO.LOW)
