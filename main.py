#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys


class SightQuiz:
    def __init__(self):
        self.width = 1280
        self.height = 640
        
        pygame.init()
        pygame.display.set_caption('Sight Quiz!')
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((255, 255, 255))
        self.sight_img = pygame.transform.scale(pygame.image.load("./img/sight.png").convert_alpha(), (50, 50))
        pygame.display.update()
    
    @staticmethod
    def is_kill():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def base(self):
        pygame.draw.circle(self.window, (255, 0, 0), (self.width / 2, self.height * 1 / 4), 150)
        pygame.draw.line(self.window, (255, 0, 0), (self.width * 1 / 6, self.height / 2),
                         (self.width / 2, self.height * 1 / 4), 50)
        
        pygame.draw.circle(self.window, (0, 0, 255), (self.width / 2, self.height * 3 / 4), 150)
        pygame.draw.line(self.window, (0, 0, 255), (self.width * 5 / 6, self.height / 2),
                         (self.width / 2, self.height * 3 / 4), 50)
        
        # pygame.draw.rect(self.window, (255, 0, 0), (0, (self.height / 2) - 50, self.width, 10))
        
        # pg.draw.rect(self.window, (255, 255, 255), (0, (self.height / 2) - 50, self.width, 100))
        pygame.draw.circle(self.window, (255, 0, 0), (self.width * 1 / 6, self.height / 2), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (self.width * 1 / 6, self.height / 2), 30)
        
        pygame.draw.circle(self.window, (0, 0, 255), (self.width * 5 / 6, self.height / 2), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (self.width * 5 / 6, self.height / 2), 30)
        
        self.window.blit(self.sight_img, (self.width * 1 / 6 - 25, self.height / 2 - 25))
        self.window.blit(self.sight_img, (self.width * 5 / 6 - 25, self.height / 2 - 25))
    
    def update(self):
        while True:
            self.is_kill()
            self.window.fill((255, 255, 255))
            self.base()
            pygame.display.update()


if __name__ == '__main__':
    sight_quiz = SightQuiz()
    sight_quiz.update()
