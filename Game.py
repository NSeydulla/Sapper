import pygame
from time import time
from random import randint

from Cell import Cell
from config import sc

class Game():
    def __init__(self, screen):
        self.active = True
        self.sc = screen
        self.cells = [[Cell(x, y) for x in range(sc.cells)] for y in range(sc.cells)]
        self.counter = sc.cells*sc.cells - sc.mines
        for i in range(sc.mines):
            while 1:
                x, y = randint(0,sc.cells-1), randint(0,sc.cells-1)
                if not self.cells[y][x].isMine:
                    self.cells[y][x].isMine = True
                    break
        for row in self.cells:
            for cell in row:
                cell.init(self.cells)
        self.sc.fill((50,50,60))
        self.draw()
        self.start = time()

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.sc)
        pygame.display.update()

    def getClickedCell(self, x, y):
        j = x // (sc.cell_size+sc.indent)
        if x >= sc.cell_size*(j+1) + sc.indent*j: return
        
        i = y // (sc.cell_size+sc.indent)
        if y >= sc.cell_size*(i+1) + sc.indent*i: return
        return i, j

    def onClick(self, x, y, isLMB):
        result = self.getClickedCell(x, y)
        if result is None: return
        cell = self.cells[result[0]][result[1]]
        if not cell.isHidden: return
        if isLMB:
            cell.isHidden = False
            cell.draw(self.sc)
            self.counter -= 1
            if cell.isMine:
                self.active = False
                self.counter += 1
                print('Lose!')
            elif cell.num == 0:
                updatedCells = cell.updateAround(self.cells)
                self.counter -= len(updatedCells)
                for cell in updatedCells:
                    cell.draw(self.sc)
        else:
            cell.isMarked = not cell.isMarked
            cell.draw(self.sc)
        if self.counter == 0:
            self.active = False
            print('win!')
        if not self.active:
            for row in self.cells:
                for cell in row:
                    cell.isHidden = False
                    cell.draw(self.sc)
        pygame.display.update()