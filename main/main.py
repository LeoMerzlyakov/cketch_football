import pygame
from screen import Screen

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GRASS_COLOR = (24, 97, 28)
MENU_COLOR = (217, 219, 211)



def start():
    pygame.init()
    pygame.display.set_caption("Sketch Football")
    clock = pygame.time.Clock()
    
    running = True
    screen = Screen().get_screen()

    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    start()

