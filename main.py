import time

import pygame
import sys
from algorithms import *
from random import randint


class Application:
    FPS = 30

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('arial', 10)
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.heights_left = [randint(1, 100) for _ in range(200)]
        self.heights_right = [randint(1, 100) for _ in range(200)]
        self.bubble_heights = []
        self.insertion_heights = []

        self.ratio = len(self.heights_left) / len(self.heights_right)
        self.timer_bubble = 0
        self.timer_insertion = 0

        #self.main_text = self.font.render(f'FPS: {self.FPS}', True, (0, 0, 0))
        self.ratio_text = self.font.render(f'Ratio: {self.ratio:.2f}', True, (0, 0, 0))
        self.left_text = self.font.render(f'Bubble Sort: {self.timer_bubble:.2f} seconds\nLength: {len(self.heights_left)}', True, (0, 0, 0))
        self.right_text = self.font.render(f'Insertion Sort: {self.timer_insertion:.2f} seconds\n Length: {len(self.heights_right)}', True, (0, 0, 0))

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def update(self):

        if self.bubble_heights != sorted(self.bubble_heights):
            self.timer_bubble = pygame.time.get_ticks() / 1000
            self.left_text = self.font.render(f'Bubble Sort: {self.timer_bubble:.2f} seconds Length: {len(self.heights_left)}', True, (0, 0, 0))

        if self.insertion_heights != sorted(self.insertion_heights):
            self.timer_insertion = pygame.time.get_ticks() / 1000
            self.right_text = self.font.render(f'Insertion Sort: {self.timer_insertion:.2f} seconds Length: {len(self.heights_right)}', True, (0, 0, 0))

        self.main_text = self.font.render(f'FPS: {self.clock.get_fps():.2f}', True, (0, 0, 0))

        self.bubble_heights = bubble_sort(self.heights_left)
        self.insertion_heights = insertion_sort(self.heights_right)

    def draw(self):
        self.screen.fill((255, 255, 255))

        for i, height in enumerate(self.bubble_heights):
            pygame.draw.rect(self.screen, (0, 0, 0), (i * 2, 200 - height * 2, 2, height * 2))

        for i, height in enumerate(self.insertion_heights):
            pygame.draw.rect(self.screen, (0, 0, 0), (i * 2 + len(self.bubble_heights) * 2, 200 - height * 2, 2, height * 2))

        self.screen.blit(self.left_text, (len(self.bubble_heights) // 2, 300))
        self.screen.blit(self.right_text, (len(self.insertion_heights) // 2 + len(self.bubble_heights) * 2, 300))
        self.screen.blit(self.ratio_text, (self.screen.get_width() // 2 - self.ratio_text.get_width() // 2, 350))
        self.screen.blit(self.main_text, (self.screen.get_width() // 2 - self.main_text.get_width() // 2, 400))

        pygame.display.flip()


if __name__ == '__main__':
    app = Application()
    app.run()
