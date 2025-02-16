# 其他人的有问题
# 我决定自己写写试试
# author: rota

import pygame
import mapp
import color

global scree_width
scree_width = 800
global scree_height
scree_height = 800

room_size = 15
steps = 0

r_list = mapp.map_list  #42*43

pygame.init()
screen = pygame.display.set_mode([scree_width,scree_height])

clock = pygame.time.Clock()


screen.fill(color.White)


user = pygame.image.load("fun_little_game/迷宫/user.png").convert_alpha()
width, height = user.get_size()
user = pygame.transform.smoothscale(user,(8,8))
width, height = user.get_size()
x = 25 + 42 * room_size
y = 25 + 9 * room_size
roomx = 42
roomy = 9
screen.blit(user, (x, y))

for i in range(42):
    for j in range(43):
        if r_list[i][j] == 3:
            pygame.draw.circle(screen,color.Red,[30 + i*room_size,30 + j*room_size],5,0)
            pygame.display.flip()
            r_list[i][j] = 0
        elif r_list[i][j] == 1:
            pygame.draw.rect(screen, color.Black, [25 + i * room_size, 25 + j * room_size, 10, 10], 0)
            pygame.display.flip()
        elif r_list[i][j] == 0:
            pygame.draw.rect(screen, color.White, [25 + i * room_size, 25 + j * room_size, 10, 10], 1)
            pygame.display.flip()
pygame.display.flip()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
