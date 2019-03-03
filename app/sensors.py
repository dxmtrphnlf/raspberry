from time import sleep
from typing import Callable

from base import InputSensor, OutputSensor

from MQTT import MQTT


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
    is_on = False
    mqtt = None

    def __init__(self, pin: int):
        super().__init__(pin)
        try:
            self.mqtt = MQTT()
        except ConnectionError:
            pass

    def listen_onclick(self, on_click_func: Callable):
        while True:
            if self.gpio.input(self.pin) == 0:
                self.is_on = not self.is_on
                self.send_button_status()
                on_click_func()
                break

    def send_button_status(self):
        message = 'Button is ON' if self.is_on else 'Button is OFF'
        self.mqtt.pulish(topic='signals/button', retain=True, payload=message)
