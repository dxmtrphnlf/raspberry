import RPi.GPIO as GPIO


class AppConfig:
    """
    Конфигурация приложения
    """

    def __init__(self, sensors: list):
        self.sensors = sensors

    def __enter__(self):
        """
        Предварительная настройка перед стартом приложения
        """
        GPIO.setmode(GPIO.BOARD)
        for s in self.sensors:
            s.setup()
        return self

    def __exit__(self, type, value, traceback):
        """
        Дейстия перед остановкой приложения
        """
        for s in self.sensors:
            s.destroy()
        GPIO.cleanup()
