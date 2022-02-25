import pygame
import config


class Player():
    def __init__(self, position_x, position_y , player):
        self.name = player
        self.position_x = position_x
        self.position_y = position_y
        self.holding = []

        if self.name == 'player_1':
            self.image = pygame.image.load('img/player_1.png')
        if self.name == 'player_2':
            self.image = pygame.image.load('img/player_2.png')
        player_2_y = 300
        player_2_x = 900
        player_2_cord = (player_2_x, player_2_y)

    def hold(self):
        for object in self.holding:
            object.position_x = self.position_x + 10
            object.position_y = self.position_y + 30

    def get_ball(self, ball):
        self.holding.append(ball)
        self.hold()

    def moves(self):
        print('aaa')

    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))
