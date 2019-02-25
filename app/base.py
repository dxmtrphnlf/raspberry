import RPi.GPIO as GPIO
from abc import ABCMeta, abstractmethod


class BaseSensor(metaclass=ABCMeta):
    """
    Абстрактный класс для всех датчиков
    pin = числовое значения пина подключения
    """
    pin = None

    @abstractmethod
    def setup(self):
        """
        Действия по предварительной настройки датчика
        """
        pass

    @abstractmethod
    def destroy(self):
        """
        Действия до удаления датчика или до остановки работы приложения
        """
        pass


class InputSensor(BaseSensor, metaclass=ABCMeta):
    """
    Абстрактный класс для датчиков, которые принимают информацию
    """

    def setup(self):
        GPIO.setup(self.pin, GPIO.IN)

    def destroy(self):
        pass


class OutputSensor(BaseSensor, metaclass=ABCMeta):
    """
    Абстрактный класс для датчиков, которые выводят информацию
    """

    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)

    def destroy(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.setup(self.pin, GPIO.LOW)
