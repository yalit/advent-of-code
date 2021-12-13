""" from matplotlib import pyplot as plt

f = open("output_13_part2.txt","r")

points = f.readlines()[0].split('#/#')
for point in points:
    [x,y] = point.split(',')
    plt.plot(int(x), -1 * int(y), marker="d", color="blue")

plt.savefig("output_13_part2.png") """


import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# get data from resolution
f = open("output_13_part2.txt","r")
points = list(map(lambda x : list(map(lambda y: int(y), x.split(','))), f.readlines()[0].split('#/#')))

maxX = 40
maxY = 6

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 60


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for point in points:
        rect = pygame.Rect(point[0]*blockSize, point[1]*blockSize,
                               blockSize, blockSize)
        pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == '__main__':
    main()