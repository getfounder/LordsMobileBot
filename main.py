import config as cfg

from classes import *
from functions import *

import os

from time import sleep

import keyboard

# Горячая клавиша для остановки при помощи вызова ошибки
keyboard.add_hotkey("ctrl+alt+p", lambda: os.__exit__)

# Инициализация окна и отображение его поверх остальных приложений
emulator_window = Window()

# Запуск самого бота
lmbot = LordsBot()
lmbot.auto_help()