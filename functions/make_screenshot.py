from PIL import ImageGrab


def make_screenshot(area, folder="screenshots", filename="screen.png"):
    # Распаковка значение с кортежа
    x0, y0, width, height = area

    # Создание скриншот с экрана в формате RGB
    rgb_image = ImageGrab.grab(bbox=(x0, y0, x0 + width, y0 + height))

    # Форматирование в 2-цветное изображение
    gray_image = rgb_image.convert('L')
    bw_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')

    # Сохранение 
    bw_image.save(f"images/{folder}/{filename}")