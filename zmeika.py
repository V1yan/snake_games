# импортируем библеотеки 
import pygame
import time
import random

snake_speed = 15

# размеры игрового окна
window_x = 720
window_y = 480

# ставим цветы 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# включаем pygame
pygame.init()

# инициализация окна игры 
pygame.display.set_caption('Карапетян Д.А._ИС24-02п_Игра_Змейка')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS контроль 
fps = pygame.time.Clock()

# расположение змейки в начале игры
snake_position = [100, 50]

# расположение всего тела змейки в начале
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# генерация яблок
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# направление змейки в начале 

direction = 'RIGHT'
change_to = direction

# начальный счёт
score = 0

# функкция для подсчёта счёта
def show_score(choice, color, font, size):
  
    # создание объекта 
    score_font = pygame.font.SysFont(font, size)
    
    # поверхность  
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # прямоугольник для текста
    # объект 
    score_rect = score_surface.get_rect()
    
    # отображение текста
    game_window.blit(score_surface, score_rect)

# функция для проигрыша
def game_over():
  
    # создание объекта шрифта
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # создание текстового места для текста игра закончена и счёт 
    
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
   # прямоугольник для текста
    # объект 
    game_over_rect = game_over_surface.get_rect()
    
    # положение текста 
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit отобразит текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # прога закроется через 2 секунды
    time.sleep(2)
    
    # выключение библеотеки 
    pygame.quit()
    
    # выход с игры
    quit()


# основ функция
while True:
    
    # оброботка происходящего и нажатие клавиш
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # делаем так чтоб при нажатии 2 кнопок смейка не порвалась в разные стороны
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # двиэение змейки 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # увелечение змейки когда она кушает
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # условия конца игры
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # если змейка сама себя коснулась
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # отображение результата
    show_score(1, white, 'times new roman', 20)

    # обновить экран игры
    pygame.display.update()

    # обновление фпс
    fps.tick(snake_speed)
