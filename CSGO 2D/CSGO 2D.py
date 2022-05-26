import pygame
import sys

def overlap(x,y,w,h,vx,vy,vw,vh):
    x2=x+w
    y2=y+h
    vx2=vx+vw 
    vy2=vy+vh
    r = (vx<=x<=vx2 or x<=vx<=x2) and (vy<=y<=vy2 or y<=vy<=y2)
    return r
# ***************** Начало игры *****************
pygame.init() # инициализируем движок
screen = pygame.display.set_mode([1000, 500]) # открываем окно на дисплее
clock = pygame.time.Clock() # создаем системный объект clock, обратимся к нему позднее для задержки игры
running = True # создаем логическую переменную-флажок, означающую, что игра выполняется


background_pic=pygame.image.load("FON.png") # подгружаем картинку фона
player_pic = pygame.image.load("GG.png") # подгружаем картинку рыбки
player_pic_left = pygame.image.load("GG_left.png")
player_x = 0 # задаем начальную координату x для картинки рыбки
player_y = 0 # задаем начальную координату y для картинки рыбки
player_size = 30
s_width = 1000 # задаем перменную ширины игрового окна
s_high = 500 # задаем переменную высоты игрового окна
enemy1_pic = pygame.image.load("enemy_1.png")
enemy1_x = 200 # задаем начальную координату x для картинки рыбки
enemy1_y = 200 # задаем начальную координату y для картинки рыбки
enemy2_pic = pygame.image.load("enemy_2.png")
enemy2_x = 800 # задаем начальную координату x для картинки рыбки
enemy2_y = 200 # задаем начальную координату y для картинки рыбки
enemy3_pic = pygame.image.load("enemy_3.png")
enemy3_x = 200 # задаем начальную координату x для картинки рыбки
enemy3_y = 50 # задаем начальную координату y для картинки рыбки
enemy4_pic = pygame.image.load("enemy_4.png")
enemy4_x = 900 # задаем начальную координату x для картинки рыбки
enemy4_y = 45 # задаем начальную координату y для картинки рыбки
enemy5_pic = pygame.image.load("enemy_5.png")
enemy5_x = 470 # задаем начальную координату x для картинки рыбки
enemy5_y = 360 # задаем начальную координату y для картинки рыбки
enemy6_pic = pygame.image.load("enemy_6.png")
enemy6_x = 50 # задаем начальную координату x для картинки рыбки
enemy6_y = 350 # задаем начальную координату y для картинки рыбки
enemy_n = 6
enemy_speed = [2]*enemy_n
enemy_size = [50]*enemy_n
enemy_x = [0]*enemy_n
enemy_y = [0]*enemy_n
BLACK = (0, 0, 0)
left_wall = pygame.Rect(-2,0,2,505)
right_wall = pygame.Rect(1930, 0, 2, 505)
top_wall = pygame.Rect(-2,-2,1005,2)
down_wall = pygame.Rect(201,950,1005,2)
wall_1 = pygame.Rect(145,10,2,155)
wall_2 = pygame.Rect(125,165,450,10)
wall_3 = pygame.Rect(100,250,150,10)


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
        pygame.image.load('GG_left.png')
        screen.blit(pygame.transform.scale(player_pic,(70,60)),(player_x,player_y))
    if keys[pygame.K_DOWN] and not player.colliderect(down_wall): # если в keys зафиксировано нажатие стрелки вниз
        player_y = player_y + 4 # увеличиваем координату y рыбки
    if keys[pygame.K_UP] and not player.colliderect(top_wall) and not player.colliderect(wall_2):
        player_y = player_y - 4 # уменьшаем координату y рыбки
    for i in range(enemy_n): # для каждого врага выполняем команды
      if overlap(player_x, player_y, int(player_size * 1.25), player_size, enemy_x[i], enemy_y[i], int(enemy_size[i] * 1.25), enemy_size[i]):
        player_size += 2
        enemy_x[i] = -200
        enemy_speed[i] = 2

    screen.blit(background_pic,(0,0))      
    screen.blit(pygame.transform.scale(player_pic,(70,60)),(player_x,player_y))
    screen.blit(pygame.transform.scale(enemy1_pic,(70,60)),(enemy1_x,enemy1_y))
    screen.blit(pygame.transform.scale(enemy2_pic,(70,60)),(enemy2_x,enemy2_y))
    screen.blit(pygame.transform.scale(enemy3_pic,(70,60)),(enemy3_x,enemy3_y))
    screen.blit(pygame.transform.scale(enemy4_pic,(80,70)),(enemy4_x,enemy4_y))
    screen.blit(pygame.transform.scale(enemy5_pic,(80,70)),(enemy5_x,enemy5_y))
    screen.blit(pygame.transform.scale(enemy6_pic,(80,70)),(enemy6_x,enemy6_y))


    
    #pygame.draw.rect(screen, BLACK, (100,250,150,10))
    pygame.display.flip() # обновляем окно дисплея, выводим в него экран с изменениями
    clock.tick(60) # делаем задержку, обновление экрана происходит на быстрее 50 раз в секунду

# ***************** Завершение игры (после выхода из основного цикла) *****************
print("The game has closed")  # уведомляем игроков о завершении игры
pygame.quit()   # останавливаем игровой движок
sys.exit()  # закрываем окно с экраном игры