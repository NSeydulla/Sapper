import pygame
from Game import Game
from config import sc

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            elif Game.active and event.type == pygame.MOUSEBUTTONDOWN:
                Game.onClick(*event.pos, event.button==1)
        clock.tick(15)

pygame.init()
screen = pygame.display.set_mode((sc.w, sc.h))
pygame.display.set_caption("Сапёр")

clock = pygame.time.Clock()
Game = Game(screen)

main()

pygame.quit()