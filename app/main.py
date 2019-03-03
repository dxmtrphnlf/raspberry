from config import AppConfig
from sensors import Laser, Button

if __name__ == '__main__':
    with AppConfig() as app_config:
        laser = Laser(7)
        button = Button(12)
        while True:
            button.listen_onclick(laser.switch)
