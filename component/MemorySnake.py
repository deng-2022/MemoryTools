import pygame
import sys
import random


# 贪吃蛇小游戏
class MemorySnake:
    def __init__(self):
        # 初始化游戏窗口大小、标题、颜色等属性
        self.screen_width = 640
        self.screen_height = 480
        pygame.display.set_caption("Memory Snake")
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        # 蛇的初始位置
        self.snake_pos = [[100, 100], [80, 100], [60, 100]]
        # 食物的初始位置
        self.food_pos = [300, 300]
        # 蛇的大小
        self.snake_size = 20
        # 食物的大小
        self.food_size = 20
        # 控制游戏速度
        self.clock = pygame.time.Clock()
        # 游戏速度
        self.speed = 12
        # 蛇的初始方向
        self.direction = "RIGHT"
        # 初始分数
        self.score = 0
        # 定义其他属性，如BLACK等
        self.BLACK = (0, 0, 0)

    # 初始化pygame并创建游戏窗口
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        while True:
            # 处理游戏事件
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

            # 更新蛇的位置
            self.update_snake_position()
            # 检测碰撞
            self.detect_collision()
            # 绘制游戏画面
            self.draw_game()
            # 更新屏幕显示
            pygame.display.flip()
            # 控制游戏速度
            self.clock.tick(self.speed)

    # 根据蛇的方向更新蛇头的位置
    def update_snake_position(self):
        if self.direction == "UP":
            new_pos = [self.snake_pos[0][0], self.snake_pos[0][1] - self.snake_size]
        elif self.direction == "DOWN":
            new_pos = [self.snake_pos[0][0], self.snake_pos[0][1] + self.snake_size]
        elif self.direction == "LEFT":
            new_pos = [self.snake_pos[0][0] - self.snake_size, self.snake_pos[0][1]]
        elif self.direction == "RIGHT":
            new_pos = [self.snake_pos[0][0] + self.snake_size, self.snake_pos[0][1]]

        # 将新位置插入到蛇身列表的开头
        self.snake_pos.insert(0, new_pos)

        # 如果蛇头与食物位置重合，吃掉食物并增加分数
        if self.snake_pos[0] == self.food_pos:
            self.food_pos = [random.randrange(1, self.screen_width // self.food_size) * self.food_size,
                             random.randrange(1, self.screen_height // self.food_size) * self.food_size]
            self.score += 1
        # 如果蛇头碰到边界或自身，游戏结束
        else:
            self.snake_pos.pop()

    # 检测蛇头是否碰到边界或自身
    def detect_collision(self):
        # 检测蛇头是否碰到边界或自身，如果是则游戏结束
        if (self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= self.screen_width or self.snake_pos[0][1] < 0 or
                self.snake_pos[0][1] >= self.screen_height or self.snake_pos[0] in self.snake_pos[1:]):
            pygame.quit()
            sys.exit()

    # 绘制游戏画面
    def draw_game(self):
        # 绘制游戏画面，包括蛇和食物
        self.screen.fill(self.WHITE)
        for pos in self.snake_pos:
            pygame.draw.rect(self.screen, self.GREEN, (pos[0], pos[1], self.snake_size, self.snake_size))
        pygame.draw.rect(self.screen, self.RED, (self.food_pos[0], self.food_pos[1], self.food_size, self.food_size))
        # 绘制分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.BLACK)
        self.screen.blit(score_text, (10, 10))
