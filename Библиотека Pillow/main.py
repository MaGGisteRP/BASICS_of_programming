from PIL import Image, ImageDraw, ImageFilter
import random

# Функция для создания случайного цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Запрос у пользователя ширины и высоты изображения
width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))

# Создание нового изображения
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Различные геометрические примитивы и текст
rectangle_width = width * 0.4
rectangle_height = height * 0.3
rectangle_position = ((width - rectangle_width) / 2, (height - rectangle_height) / 2)
draw.rectangle([rectangle_position, (rectangle_position[0] + rectangle_width, rectangle_position[1] + rectangle_height)], fill=random_color())

polygon_points = [
    (width * 0.1, height * 0.1),
    (width * 0.2, height * 0.2),
    (width * 0.3, height * 0.3),
    (width * 0.1, height * 0.3)
]
draw.polygon(polygon_points, fill=random_color())

ellipse_width = width * 0.6
ellipse_height = height * 0.4
ellipse_position = ((width - ellipse_width) / 2, (height - ellipse_height) / 2)
draw.ellipse([ellipse_position, (ellipse_position[0] + ellipse_width, ellipse_position[1] + ellipse_height)], fill=random_color())

text = "Пример текста"
draw.text((width * 0.1, height * 0.8), text, fill=random_color())

# Сохранение изображения до применения фильтра
image.save("original_image.png")

# Применение фильтра к изображению
filtered_image = image.filter(ImageFilter.BLUR)

# Сохранение измененного изображения
filtered_image.save("filtered_image.png")