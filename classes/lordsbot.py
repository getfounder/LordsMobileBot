import config as cfg

from functions import *

from time import sleep

import pyautogui


class LordsBot:
    def __init__(self, type=None):
        self.type = type

    def auto_help(self):
        width, height = [count // 2 for count in cfg.areas["for_templates"]["hands"][2::]]

        dx = cfg.areas["hands"][0] + width
        dy = cfg.areas["hands"][1] + height

        while True:
            make_screenshot(cfg.areas["hands"], filename="hands.png")

            result_array = search_template(cfg.paths["scr"]["hands"], cfg.paths["tmp"]["hands"], threshold=0.9)
            sleep(1)
            
            for values in result_array:
                if len(values) == 0:
                    break
            else:
                x, y = [values[0] for values in result_array]

                pyautogui.moveTo(dx + x, dy + y, duration=cfg.DEFAULT_TIME_DURATION)
                pyautogui.click()
                sleep(cfg.DEFAULT_TIME_SLEEP)

                pyautogui.moveTo(cfg.buttons["help_everyone"], duration=cfg.DEFAULT_TIME_DURATION)
                pyautogui.click()
                sleep(cfg.DEFAULT_TIME_SLEEP)

                pyautogui.moveTo(cfg.buttons["cross_help"], duration=cfg.DEFAULT_TIME_DURATION)
                pyautogui.click()
                sleep(cfg.DEFAULT_TIME_SLEEP)
