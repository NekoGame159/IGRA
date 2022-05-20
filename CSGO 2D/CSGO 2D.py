import pygame
import sys


# ***************** Начало игры *****************
pygame.init() # инициализируем движок
screen = pygame.display.set_mode([1000, 500]) # открываем окно на дисплее
clock = pygame.time.Clock() # создаем системный объект clock, обратимся к нему позднее для задержки игры
running = True # создаем логическую переменную-флажок, означающую, что игра выполняется


background_pic=pygame.image.load("FON.png") # подгружаем картинку фона
player_pic = pygame.image.load("GG.png") # подгружаем картинку рыбки
player_x = 0 # задаем начальную координату x для картинки рыбки
player_y = 0 # задаем начальную координату y для картинки рыбки
s_width = 1000 # задаем перменную ширины игрового окна
s_high = 500 # задаем переменную высоты игрового окна
left_wall = pygame.Rect(-2,0,2,505)
right_wall = pygame.Rect(1930, 0, 2, 505)
top_wall = pygame.Rect(-2,-2,1005,2)
down_wall = pygame.Rect(201,950,1005,2)
wall_1 = pygame.Rect(145,10,2,155)
wall_2 = pygame.Rect(2,2,400,2)

# ***************** Основной цикл игры *****************
# Все ниже 'while running' будет повторяться бесконечно, пока не закроете окно (т.е. когда running станет = False)
while running:
    for event in pygame.event.get(): # проверяем все системные события игры в списке pygame.event.get()
        if event.type == pygame.QUIT:  # если нашли событие, связаное с закрытием окна, то...
            running = False # сбрасываем переменную-флажок в значение ЛОЖЬ для выхода из основного цикла
            
    player = pygame.Rect(player_x, player_y, s_width, s_high)
    keys = pygame.key.get_pressed() # запрашиваем состояние клавиатуры и запоминаем в keys
    if keys[pygame.K_RIGHT] and not player.colliderect(right_wall) and not player.colliderect(wall_1):
        player_x = player_x + 4 # увеличиваем координату x рыбки
    if keys[pygame.K_LEFT] and not player.colliderect(left_wall):
        player_x = player_x - 4  # уменьшаем координату x рыбки
    if keys[pygame.K_DOWN] and not player.colliderect(down_wall): # если в keys зафиксировано нажатие стрелки вниз
        player_y = player_y + 4 # увеличиваем координату y рыбки
    if keys[pygame.K_UP] and not player.colliderect(top_wall) and not player.colliderect(wall_2): # если в keys зафиксировано нажатие стрелки вверх
        player_y = player_y - 4 # уменьшаем координату y рыбки       

    screen.blit(background_pic,(0,0))      
    screen.blit(pygame.transform.scale(player_pic,(70,60)),(player_x,player_y))
    
    pygame.display.flip() # обновляем окно дисплея, выводим в него экран с изменениями
    clock.tick(60) # делаем задержку, обновление экрана происходит на быстрее 50 раз в секунду

# ***************** Завершение игры (после выхода из основного цикла) *****************
print("The game has closed")  # уведомляем игроков о завершении игры
pygame.quit()   # останавливаем игровой движок
sys.exit()  # закрываем окно с экраном игры
