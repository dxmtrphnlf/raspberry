from config import AppConfig
from sensors import Laser, Button

if __name__ == '__main__':
    laser = Laser(7)
    button = Button(12)
    with AppConfig() as app_config:
        while True:
            button.listen_onclick(laser.switch)
