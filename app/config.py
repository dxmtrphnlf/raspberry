import RPi.GPIO as GPIO

from types import TracebackType
from typing import Optional, Type


class AppConfig:

    def __enter__(self):
        """
        Pre-setting before starting the application
        """
        GPIO.setmode(GPIO.BOARD)
        return self

    def __exit__(self, type: Optional[Type[BaseException]], value: Optional[BaseException],
                 traceback: Optional[TracebackType]):
        """
        Action before stopping the application
        """
        GPIO.cleanup()
