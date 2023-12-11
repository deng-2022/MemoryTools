import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("贪吃蛇")

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇的初始位置
snake_pos = [[100, 100], [80, 100], [60, 100]]

# 食物的初始位置
food_pos = [300, 300]

# 设置蛇和食物的大小
snake_size = 20
food_size = 20

# 设置游戏速度
clock = pygame.time.Clock()
speed = 12

# 设置蛇的移动方向
direction = "RIGHT"

while True:
    # 检测按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # 更新蛇的位置
    if direction == "UP":
        new_pos = [snake_pos[0][0], snake_pos[0][1] - snake_size]
    elif direction == "DOWN":
        new_pos = [snake_pos[0][0], snake_pos[0][1] + snake_size]
    elif direction == "LEFT":
        new_pos = [snake_pos[0][0] - snake_size, snake_pos[0][1]]
    elif direction == "RIGHT":
        new_pos = [snake_pos[0][0] + snake_size, snake_pos[0][1]]
    snake_pos.insert(0, new_pos)
    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(1, screen_width // food_size) * food_size,
                    random.randrange(1, screen_height // food_size) * food_size]
    else:
        snake_pos.pop()

    # 检测碰撞边界和自身碰撞
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or snake_pos[0][1] < 0 or snake_pos[0][
        1] >= screen_height or snake_pos[0] in snake_pos[1:]):
        pygame.quit()
        sys.exit()

    # 绘制游戏画面
    screen.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], food_size, food_size))
    pygame.display.flip()
    clock.tick(speed)
