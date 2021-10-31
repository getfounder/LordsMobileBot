import cv2
import numpy as np


def search_template(base_image, template, threshold=0.9):
    # Открытие 1-битовых изображений
    img = cv2.imread(base_image)
    tmp = cv2.imread(template)

    # Поиск шаблона на картинке
    res = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)

    # Получение валидных координат
    matches = np.where(res >= threshold)
    return np.array([np.asarray(matches[1]), np.asarray(matches[0])])