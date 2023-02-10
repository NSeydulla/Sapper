import pygame
from config import sc

pygame.font.init()
font = pygame.font.Font(None, int(sc.cell_size*0.9))

def text_speech(sc, text, color, pos):
    rendered_text = font.render(text, True, color)
    sc.blit(rendered_text, rendered_text.get_rect(center=pos))
colors = [(50,255,50), (50,50,255), (255,255,50), (230, 100, 100), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]

class Cell():
    def __init__(self, x, y):
        self.isHidden = True
        self.isMarked = False
        self.isMine = False
        self.x, self.y = x, y
        self.num = 0

    def init(self, cells):
        if self.isMine: return
        for x in range(self.x-1,self.x+2):
            if not 0<=x<sc.cells: continue
            for y in range(self.y-1,self.y+2):
                if not 0<=y<sc.cells: continue
                if cells[y][x].isMine: self.num+=1

    def updateAround(self, cells):
        updatedCells = []
        for x in range(self.x-1,self.x+2):
            if not 0<=x<sc.cells: continue
            for y in range(self.y-1,self.y+2):
                if not 0<=y<sc.cells or (x==self.x and y==self.y): continue
                cell = cells[y][x]
                if cell.isHidden:
                    cell.isHidden = False
                    updatedCells.append(cell)
                    if cell.num == 0:
                        updatedCells += cell.updateAround(cells)
        return updatedCells

    def draw(self, screen, x=None, y=None):
        if x is None: x = self.x*sc.cell_size+self.x*sc.indent
        if y is None: y = self.y*sc.cell_size+self.y*sc.indent
        rect = (x, y, sc.cell_size, sc.cell_size)
        if self.isHidden:
            return pygame.draw.rect(screen, (220,80,80) if self.isMarked else (220,220,220), rect)
        pygame.draw.rect(screen, (140,140,140), rect)
        textRect = (x+sc.cell_size//2,y+sc.cell_size//2)
        if self.isMine: text_speech(screen, '@', (255,0,0), textRect)
        elif self.num>0: text_speech(screen, str(self.num), colors[self.num-1], textRect)