import random
import os
import pygame

WIDTH, HEIGHT = 320, 320
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
U_WIDTH = WIDTH//8
U_HEIGHT = HEIGHT//8
number_of_bombs = 11
bombs_pos = []
bombs = []
level = []
covering_tiles = []
flags = []
empty_spots = []
clock = pygame.time.Clock()
pygame.display.set_caption("snake")
num_0 = pygame.image.load(os.path.join('liczby', '0.png'))
num_1 = pygame.image.load(os.path.join('liczby', '1.png'))
num_2 = pygame.image.load(os.path.join('liczby', '2.png'))
num_3 = pygame.image.load(os.path.join('liczby', '3.png'))
num_4 = pygame.image.load(os.path.join('liczby', '4.png'))
num_5 = pygame.image.load(os.path.join('liczby', '5.png'))
num_6 = pygame.image.load(os.path.join('liczby', '6.png'))
num_7 = pygame.image.load(os.path.join('liczby', '7.png'))
num_8 = pygame.image.load(os.path.join('liczby', '8.png'))
flag_image = pygame.image.load(os.path.join('liczby', 'flag.png'))
bomb_image = pygame.image.load(os.path.join('liczby', 'mina.png'))
tile_image = pygame.image.load(os.path.join('liczby', 'tile.png'))

for i in range(number_of_bombs):
    sup = random.randrange(64)
    print(sup)
    sup = str(sup)
    while sup in bombs_pos:
        sup = random.randrange(64)
        print("again", sup)
        sup = str(sup)
    bombs_pos.append(sup)

print(bombs_pos)
for i in range(len(bombs_pos)):
    bombs_pos[i] = int(bombs_pos[i])


class Bomb(object):

    def __init__(self, pos):
        bombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], U_WIDTH, U_HEIGHT)


class CoverTile(object):
    def __init__(self, pos_tile):
        covering_tiles.append(self)
        self.rect = pygame.Rect(pos_tile[0], pos_tile[1], U_WIDTH, U_HEIGHT)


class Flag(object):
    def __init__(self, pos_flag):
        flags.append(self)
        self.rect = pygame.Rect(pos_flag[0], pos_flag[1], U_WIDTH, U_HEIGHT)


class Empty(object):
    def __init__(self, pos_empty):
        empty_spots.append(self)
        self.rect = pygame.Rect(pos_empty[0], pos_empty[1], U_WIDTH, U_HEIGHT)


for i in range(8):
    row = ''
    for a in range(8):

        if (i*8 + a) in bombs_pos:

            row += "x"
        else:
            row += ' '
    level.append(row)


def draw_scene(level, bombs, covering_tiles, flags):
    WIN.fill((0, 0, 0))
    for bomb in bombs:
        pygame.draw.rect(WIN, (255, 255, 255), bomb.rect)

    x = y = 0
    for row in level:
        for col in row:
            if col == "0":
                WIN.blit(num_0, (U_WIDTH*x, U_HEIGHT*y))
            if col == "1":
                WIN.blit(num_1, (U_WIDTH*x, U_HEIGHT*y))
            if col == "2":
                WIN.blit(num_2, (U_WIDTH*x, U_HEIGHT*y))
            if col == "3":
                WIN.blit(num_3, (U_WIDTH*x, U_HEIGHT*y))
            if col == "4":
                WIN.blit(num_4, (U_WIDTH*x, U_HEIGHT*y))
            if col == "5":
                WIN.blit(num_5, (U_WIDTH*x, U_HEIGHT*y))
            if col == "6":
                WIN.blit(num_6, (U_WIDTH*x, U_HEIGHT*y))
            if col == "7":
                WIN.blit(num_7, (U_WIDTH*x, U_HEIGHT*y))
            if col == "8":
                WIN.blit(num_8, (U_WIDTH*x, U_HEIGHT*y))
            if col == "x":
                WIN.blit(bomb_image, (U_WIDTH * x, U_HEIGHT * y))
            x += 1
        x = 0
        y += 1
    for covering_tile in covering_tiles:
        WIN.blit(tile_image, (covering_tile.rect.x, covering_tile.rect.y))

    for flag in flags:
        WIN.blit(flag_image, (flag.rect.x, flag.rect.y))
    pygame.display.flip()


def number_bombs_nearby(row_num, pos):
    num = 0
    row = level[row_num]

    if row == level[0]:
        row_next = level[row_num + 1]
        if pos == 0:
            if row[pos + 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos + 1] =="x":
                num += 1
        elif pos != 0 and pos != 7:
            if row[pos - 1] == "x":
                num += 1
            if row[pos + 1] == "x":
                num += 1
            if row_next[pos - 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos + 1] == "x":
                num += 1
        else:
            if row[pos - 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos - 1] == "x":
                num += 1
    elif row_num != 0 and row_num != 7:
        row_next = level[row_num + 1]
        row_prev = level[row_num - 1]
        if pos == 0:
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos + 1] == "x":
                num += 1
            if row[pos + 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos + 1] == "x":
                num += 1
        elif pos != 0 and pos != 7:
            if row_prev[pos - 1] == "x":
                num += 1
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos + 1] == "x":
                num += 1
            if row[pos - 1] == "x":
                num += 1
            if row[pos + 1] == "x":
                num += 1
            if row_next[pos - 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos + 1] == "x":
                num += 1
        else:
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos - 1] == "x":
                num += 1
            if row[pos - 1] == "x":
                num += 1
            if row_next[pos] == "x":
                num += 1
            if row_next[pos - 1] == "x":
                num += 1
    elif row == level[7]:
        row_prev = level[row_num - 1]
        if pos == 0:
            if row[pos + 1] == "x":
                num += 1
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos + 1] =="x":
                num += 1
        elif pos != 0 and pos != 7:
            if row[pos - 1] == "x":
                num += 1
            if row[pos + 1] == "x":
                num += 1
            if row_prev[pos - 1] == "x":
                num += 1
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos + 1] == "x":
                num += 1
        else:
            if row[pos - 1] == "x":
                num += 1
            if row_prev[pos] == "x":
                num += 1
            if row_prev[pos - 1] == "x":
                num += 1
    return num


def empty_spots_chain(empty_pos, covering_tiles):
    removals = []
    for covering_tile in covering_tiles:
        if covering_tile.rect.x == empty_pos[0] - U_WIDTH and covering_tile.rect.y == empty_pos[1] - U_HEIGHT:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] and covering_tile.rect.y == empty_pos[1] - U_HEIGHT: # top middle
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] + U_WIDTH and covering_tile.rect.y == empty_pos[1] - U_HEIGHT:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] - U_WIDTH and covering_tile.rect.y == empty_pos[1]:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] + U_WIDTH and covering_tile.rect.y == empty_pos[1]:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] - U_WIDTH and covering_tile.rect.y == empty_pos[1] + U_HEIGHT:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] and covering_tile.rect.y == empty_pos[1] + U_HEIGHT:
            removals.append(covering_tile)
        if covering_tile.rect.x == empty_pos[0] + U_WIDTH and covering_tile.rect.y == empty_pos[1] + U_HEIGHT:
            removals.append(covering_tile)
    for removal in removals:
        if removal in covering_tiles:
            covering_tiles.remove(removal)
        for empty_spot in empty_spots:
            if removal.rect.x == empty_spot.rect.x and removal.rect.y == empty_spot.rect.y:
                covering_tiles = empty_spots_chain((removal.rect.x, removal.rect.y), covering_tiles)
    return covering_tiles





for i in range(len(level)):
    r_row = ""
    for a in range(len(level[i])):
        if level[i][a] == "x":
            r_row += level[i][a]
        elif level[i][a] == " ":
            r_row += str(number_bombs_nearby(i, a))
    level[i] = r_row
    print(r_row)


x = y = 0
for row in level:

    for col in row:
        if col == "x":
            Bomb((x, y))
        if col == "0":
            Empty((x, y))
        CoverTile((x, y))
        x += U_WIDTH
    y += U_HEIGHT
    x = 0

print(len(empty_spots))
# main
running = True
while running:
    mouse = pygame.mouse.get_pos()
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                flag_remove = False
                for flag in flags:
                    if (flag.rect.x + U_WIDTH) >= mouse[0] >= flag.rect.x and (flag.rect.y + U_HEIGHT) >= mouse[1] >= flag.rect.y:
                        flags.remove(flag)
                        flag_remove = True
                        break
                if not flag_remove:
                    for covering_tile in covering_tiles:
                        if (covering_tile.rect.x + U_WIDTH) >= mouse[0] >= covering_tile.rect.x and (covering_tile.rect.y + U_HEIGHT) >= mouse[1] >= covering_tile.rect.y:
                            covering_tiles.remove(covering_tile)
                            for bomb in bombs:
                                if covering_tile.rect.x == bomb.rect.x and covering_tile.rect.y == bomb.rect.y:
                                    print("soup")
                                    running = False
                            for empty_spot in empty_spots:
                                if covering_tile.rect.x == empty_spot.rect.x and covering_tile.rect.y == empty_spot.rect.y:
                                    empty_pos = [empty_spot.rect.x, empty_spot.rect.y]
                                    covering_tiles = empty_spots_chain(empty_pos, covering_tiles)
                            break
            elif e.button == 3 and len(flags) < number_of_bombs:
                for covering_tile in covering_tiles:
                    if (covering_tile.rect.x + U_WIDTH) >= mouse[0] >= covering_tile.rect.x and (covering_tile.rect.y + U_HEIGHT) >= mouse[1] >= covering_tile.rect.y:
                        overlapping = False
                        for flag in flags:
                            if covering_tile.rect.x == flag.rect.x and covering_tile.rect.y == flag.rect.y:
                                overlapping = True
                                break
                        if not overlapping:
                            Flag((covering_tile.rect.x, covering_tile.rect.y))
    if len(covering_tiles) == len(bombs):
        print("victory has been achieved")

    draw_scene(level, bombs, covering_tiles, flags)
