from config import AppConfig
from sensors import Laser, Button

if __name__ == '__main__':
    laser = Laser()
    button = Button()
    with AppConfig([laser, button]) as app_config:
        while True:
            button.listen_onclick(laser.switch)
