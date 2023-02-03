import os
import random
import sys

import pygame
import requests

slide = "http://static-maps.yandex.ru/1.x/?ll=80.137117,68.470624&z=3&l=sat"
response = requests.get(slide)
if not response:
    print("Ошибка выполнения запроса:")
    print(slide)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = 'Data/maps/map.png'
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
ind = 0
# Переключаем экран и ждем закрытия окна.
names = []
mapImage = pygame.image.load('Data/maps/map.png')
pygame.display.flip()
run = True
while run:
    screen.fill(pygame.Color('black'))
    screen.blit(mapImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
os.remove('Data/maps/map.png')
