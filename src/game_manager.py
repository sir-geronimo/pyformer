import pygame, sys


class GameManager():
    clock = None

    def __init__(self):
        pygame.init()

    def init_screen(self, title, screen_size,):
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        return pygame.display.set_mode(screen_size)

    def quit(self):
        pygame.quit()
        sys.exit()

    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()