from time import sleep
from typing import Callable

from base import InputSensor, OutputSensor


class Laser(OutputSensor):
    _delay = 0.5

    def __init__(self, pin: int):
        super(Laser, self).__init__(pin)
        self.light_state = self.gpio.LOW

    def switch(self):
        sleep(self._delay)
        if self.light_state == self.gpio.HIGH:
            self.turn_on()
        else:
            self.turn_of()

    def turn_on(self):
        self.light_state = self.gpio.LOW
        self.gpio.output(self.pin, self.gpio.LOW)

    def turn_of(self):
        self.light_state = self.gpio.HIGH
        self.gpio.output(self.pin, self.gpio.HIGH)


class Button(InputSensor):

    def listen_onclick(self, on_click_func: Callable):
        while True:
            if self.gpio.input(self.pin) == 0:
                on_click_func()
                break
