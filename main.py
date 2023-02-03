import os
import random
import sys

import pygame
import requests

slides = [
    "http://static-maps.yandex.ru/1.x/?ll=37.656680,55.719088&spn=0.302,0.302&l=sat",
    "http://static-maps.yandex.ru/1.x/?ll=131.137117,-28.470624&spn=30.902,30.502&l=sat",
    "http://static-maps.yandex.ru/1.x/?ll=80.137117,68.470624&spn=30.902,30.502&l=sat"
    ]
for i in range(len(slides)):
    response = requests.get(slides[i])
    if not response:
        print("Ошибка выполнения запроса:")
        print(slides[i])
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = str(random.randrange(0, 999999999999)) + '.png'
    with open(map_file, "wb") as file:
        file.write(response.content)
    slides[i] = map_file

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
ind = 0
# Переключаем экран и ждем закрытия окна.
names = []
for ind in range(len(slides)):
    names.append(slides[ind])
    slides[ind] = pygame.image.load(slides[ind])
pygame.display.flip()
run = True
while run:
    # screen.fill(pygame.Color('black'))
    screen.blit(slides[ind], (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            ind += 1
            ind %= len(slides)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
# Удаляем за собой файл с изображением.
for i in names:
    os.remove(i)
