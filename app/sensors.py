from time import sleep

import RPi.GPIO as GPIO

from base import InputSensor, OutputSensor


class Laser(OutputSensor):
    pin = 7
    _turn_on_state = GPIO.LOW
    _turn_off_state = GPIO.HIGH
    _delay = 0.5

    def __init__(self):
        self.light_state = GPIO.LOW

    def switch(self):
        sleep(self._delay)
        if self.light_state == self._turn_off_state:
            self.turn_on()
        else:
            self.turn_of()

    def turn_on(self):
        self.light_state = self._turn_on_state
        GPIO.output(self.pin, self._turn_on_state)

    def turn_of(self):
        self.light_state = self._turn_off_state
        GPIO.output(self.pin, self._turn_off_state)


class Button(InputSensor):
    pin = 12

    def listen_onclick(self, on_click_func):
        while True:
            if GPIO.input(self.pin) == 0:
                on_click_func()
                break
