import pygame
import sys
import random

# 贪吃蛇
class MemorySnake:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        pygame.display.set_caption("贪吃蛇")
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.snake_pos = [[100, 100], [80, 100], [60, 100]]
        self.food_pos = [300, 300]
        self.snake_size = 20
        self.food_size = 20
        self.clock = pygame.time.Clock()
        self.speed = 12
        self.direction = "RIGHT"
        self.score = 0  # 添加分数属性
        # 其他初始化代码
        self.BLACK = (0, 0, 0)  # 定义BLACK属性为黑色

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"

            self.update_snake_position()
            self.detect_collision()
            self.draw_game()
            pygame.display.flip()
            self.clock.tick(self.speed)

    def update_snake_position(self):
        if self.direction == "UP":
            new_pos = [self.snake_pos[0][0], self.snake_pos[0][1] - self.snake_size]
        elif self.direction == "DOWN":
            new_pos = [self.snake_pos[0][0], self.snake_pos[0][1] + self.snake_size]
        elif self.direction == "LEFT":
            new_pos = [self.snake_pos[0][0] - self.snake_size, self.snake_pos[0][1]]
        elif self.direction == "RIGHT":
            new_pos = [self.snake_pos[0][0] + self.snake_size, self.snake_pos[0][1]]
        self.snake_pos.insert(0, new_pos)
        if self.snake_pos[0] == self.food_pos:
            self.food_pos = [random.randrange(1, self.screen_width // self.food_size) * self.food_size,
                             random.randrange(1, self.screen_height // self.food_size) * self.food_size]
            self.score += 1  # 吃掉食物，分数加一
        else:
            self.snake_pos.pop()

    def detect_collision(self):
        if (self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= self.screen_width or self.snake_pos[0][1] < 0 or
                self.snake_pos[0][
                    1] >= self.screen_height or self.snake_pos[0] in self.snake_pos[1:]):
            pygame.quit()
            sys.exit()

    def draw_game(self):
        self.screen.fill(self.WHITE)
        for pos in self.snake_pos:
            pygame.draw.rect(self.screen, self.GREEN, (pos[0], pos[1], self.snake_size, self.snake_size))
        pygame.draw.rect(self.screen, self.RED, (self.food_pos[0], self.food_pos[1], self.food_size, self.food_size))
        # 绘制分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.BLACK)
        self.screen.blit(score_text, (10, 10))
 