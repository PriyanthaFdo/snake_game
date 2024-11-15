import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


# Snake and Food classes
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        new_head = (
            (head_x + self.direction[0]) % GRID_WIDTH,
            (head_y + self.direction[1]) % GRID_HEIGHT,
        )

        if not self.grow:
            self.positions.pop()
        self.positions.insert(0, new_head)
        self.grow = False

    def change_direction(self, direction):
        # Prevent moving back into the opposite direction
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def head_position(self):
        return self.positions[0]


class Food:
    def __init__(self, super_food=False):
        self.position = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1),
        )
        self.super_food = super_food
        self.spawn_time = time.time() if super_food else None

    def new_position(self, snake_positions):
        while self.position in snake_positions:
            self.position = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1),
            )


# Game Functions
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))


def draw_snake(snake):
    for segment in snake.positions[1:]:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
        )
    head = snake.head_position()
    pygame.draw.rect(
        screen, YELLOW, (head[0] * GRID_SIZE, head[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )


def draw_food(food):
    color = RED if not food.super_food else BLUE
    pygame.draw.rect(
        screen,
        color,
        (
            food.position[0] * GRID_SIZE,
            food.position[1] * GRID_SIZE,
            GRID_SIZE,
            GRID_SIZE,
        ),
    )


def display_score(score):
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def display_super_food_timer(remaining_time):
    font = pygame.font.SysFont(None, 30)
    timer_text = font.render(f"Super Food Time: {int(remaining_time)}", True, WHITE)
    screen.blit(timer_text, (10, 40))


# Main Game Loop
def game_loop():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    super_food = None
    normal_food_counter = 0
    score = 0

    while True:
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        display_score(score)

        if super_food:
            draw_food(super_food)
            remaining_time = 10 - (time.time() - super_food.spawn_time)
            if remaining_time > 0:
                display_super_food_timer(remaining_time)
            else:
                super_food = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.move()

        # Check for food consumption
        if snake.head_position() == food.position:
            snake.grow_snake()
            food.new_position(snake.positions)
            score += 1
            normal_food_counter += 1

            # Spawn super food after 5-10 normal foods
            if normal_food_counter >= random.randint(5, 10):
                super_food = Food(super_food=True)
                super_food.new_position(snake.positions)
                normal_food_counter = 0

        # Check for super food consumption
        if super_food and snake.head_position() == super_food.position:
            snake.grow_snake()
            score += 3  # Super food gives extra points
            super_food = None

        # Check for self-collision
        if snake.head_position() in snake.positions[1:]:
            print("Game Over! Your score:", score)
            pygame.quit()
            return

        pygame.display.flip()
        clock.tick(10)


game_loop()
