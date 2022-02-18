from curses.textpad import rectangle
from dataclasses import field
from mimetypes import init
import pygame

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GRASS_COLOR = (24, 97, 28)
MENU_COLOR = (217, 219, 211)

class Screen:
    def __init__(self) -> None:
        size = (700, 700)
        self.screen = pygame.display.set_mode(size)
        self._drow_field()
        self._drow_menu()

    def get_screen(self):
        return self.screen
    
    def _drow_field(self):
        pygame.draw.rect(self.screen, GRASS_COLOR, [0, 0, 400, 700], 0)
        greed = self._make_grid_points()
        for point in greed:
            print(point)
            pygame.draw.circle(self.screen, center=point, radius=2, color=MENU_COLOR)

        field_corners = [
            (50, 50),
            (320, 50),
            (320, 320),
            (50, 320),
        ]
        pygame.draw.lines(self.screen, color=MENU_COLOR, points=field_corners, closed=True, width=2)


    def _make_grid_points(self) -> list:
        greed = Greed()
        return greed.get_points()

    def _drow_menu(self):
        pygame.draw.rect(self.screen, MENU_COLOR, [350, 0, 700, 700], 0)

class Greed:
    def __init__(self) -> None:
        self.points = []
        self._make_points()


    def get_points(self) -> list:
        return self.points
    
    def _make_points(self) -> None:
        for point_y in range(50, 330, 30):
            for point_x in range(50, 330, 30):
                point = (point_x, point_y)
                self.points.append(point)
