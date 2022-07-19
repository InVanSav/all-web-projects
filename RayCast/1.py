import pygame
from random import*

FPS = 60
run = True
clock = pygame.time.Clock()
width = 640
height = 360
amount = 100


class GameManager:
    def __init__(self, game_window, array):
        self.game_window = game_window
        self.array = array

    def redraw(self):
        self.game_window.fill((0, 0, 0))
        for star in self.array:
            star.set_new_position()


class Star:
    def __init__(self, game_window, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.game_window = game_window
        self.draw()

    def draw(self):
        pygame.draw.circle(self.game_window, (255, 0, 0),
                          [self.x, self.y], 3)

    def set_new_position(self):
        self.x += 1
        self.y += 1
        self.draw()

pygame.init()
win = pygame.display.set_mode((width, height))

array = [Star(win, randint(0, width),
                        randint(0, height)) for i in range(amount)]

manager = GameManager(win, array)
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    manager.redraw()
    pygame.display.flip()
pygame.quit()