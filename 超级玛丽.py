import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置屏幕大小和标题
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("精简可爱版超级玛丽")

# 加载图片资源
bg = pygame.image.load("background.png").convert()
mario = pygame.image.load("mario.png").convert_alpha()

# 设置玛丽的初始位置
mario_rect = mario.get_rect()
mario_rect.topleft = (100, 100)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mario_rect.x -= 10
            elif event.key == K_RIGHT:
                mario_rect.x += 10
            elif event.key == K_UP:
                mario_rect.y -= 10
            elif event.key == K_DOWN:
                mario_rect.y += 10

    # 绘制背景和玛丽
    screen.blit(bg, (0, 0))
    screen.blit(mario, mario_rect)
    pygame.display.update()

# 退出游戏
pygame.quit()
