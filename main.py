import pygame as pg
import sys


class SightQuiz:
    def __init__(self):
        pg.init()
        pg.display.set_mode((400, 300))
        pg.display.set_caption('Hello World!')
    
    def updata(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


if __name__ == '__main__':
    sight_quiz = SightQuiz()
    sight_quiz.updata()
