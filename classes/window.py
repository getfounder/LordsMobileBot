import config as cfg

import win32gui


class Window:
    def __init__(self, name_of_emulator_window="BlueStacks"):
        # Распаковка значений из кортежей конфига
        (x0, y0), (width, height) = cfg.WINDOW_POS, cfg.WINDOW_SIZE

        # Изменение размеров окна эмулятора под значения конфига
        self.hwnd = win32gui.FindWindow(None, name_of_emulator_window)
        win32gui.MoveWindow(self.hwnd, x0, y0, x0 + width, y0 + height, True)

        # Отображение окна поверх остальных
        win32gui.SetForegroundWindow(self.hwnd)