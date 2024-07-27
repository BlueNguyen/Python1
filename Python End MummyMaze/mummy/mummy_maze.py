import pygame
import sys
from pygame.locals import *

from bfs import Graph
import json

# Đọc file JSON
with open('./mummy/map.json', 'r') as file:
    dataMap = json.load(file)


def getKey(X, Y):
    for item in dataMap:
        if item['X'] == X and item['Y'] == Y:
            return item['key']


def getLocat(key):

    return {"X": dataMap[key]['X'], "Y": dataMap[key]['Y']}


# Sử dụng
graph = Graph(6, 6)
graph.addRectangleEdges()


pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 600))


pygame.display.set_caption("Mummy maze !!")

surfaceMap = pygame.transform.scale(
    pygame.image.load("./mummy/image/floor.jpg"), (600, 600))


# (0,0) - (60,0) - (120, 0) - (180 , 0) - (240, 0)

playerUp = pygame.image.load("./mummy/image/player/move_up.png")
playerDown = pygame.image.load("./mummy/image/player/move_down.png")
playerLeft = pygame.image.load("./mummy/image/player/move_left.png")
playerRight = pygame.image.load("./mummy/image/player/move_right.png")

TIME = 5


mummyUp = pygame.image.load("./mummy/image/mummy/redup.png")
mummyDown = pygame.image.load("./mummy/image/mummy/reddown.png")
mummyLeft = pygame.image.load("./mummy/image/mummy/redleft.png")
mummyRight = pygame.image.load("./mummy/image/mummy/redright.png")

wallX, wallY, wallW, wallH = 400, 200, 10, 100
wallX2, wallY2, wallW2, wallH2 = 200, 300, 10, 100
wallX3, wallY3, wallW3, wallH3 = 200, 400, 100, 7
# Victory and Game Over Images
VICTORY_IMAGE = pygame.transform.scale(
    pygame.image.load('./mummy/image/victory.png'), (600, 600))
GAME_OVER_IMAGE = pygame.transform.scale(
    pygame.image.load('./mummy/image/game_over.png'), (600, 600))

# Hình exit 1
EXIT_IMAGE = pygame.transform.scale(
    pygame.image.load('./mummy/image/exit.png'), (100, 30))
exit_x, exit_y = 200, 570

# Hình exit 2
EXIT_IMAGE2 = pygame.transform.scale(
    pygame.image.load('./mummy/image/exit2.png'), (30, 100))
exit_x2, exit_y2 = 570, 200

# Hình bẫy game
TRAP_IMAGE = pygame.transform.scale(
    pygame.image.load('./mummy/image/trap.png'), (100, 100)).convert_alpha()  # Điều chỉnh kích thước hình bẫy theo ý muốn
trap_x, trap_y = 0, 100     # Toạ độ vị trí bẫy

trap_surface = pygame.Surface(TRAP_IMAGE.get_size(), pygame.SRCALPHA)
trap_surface.fill((255, 255, 255, 0))
trap_surface.blit(TRAP_IMAGE, (0, 0))
trap_surface = pygame.transform.scale(trap_surface, (100, 100))



class Player:
    mummyGo = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(playerDown, (20, 20), (0, 0, 60, 60))
        self.timeSkip = 0
        self.option = 0

        self.go = 0

    def update(self, up, down, left, right):

        if Player.mummyGo == 0:
            if self.go < 100:

                if self.timeSkip <= TIME:  # 0 - 5
                    self.option = 0
                elif self.timeSkip <= TIME*2:  # 6 - 10
                    self.option = 1
                elif self.timeSkip <= TIME*3:  # 11 - 15
                    self.option = 2
                elif self.timeSkip <= TIME*4:
                    self.option = 3
                elif self.timeSkip <= TIME*5:
                    self.option = 4

                elif self.timeSkip > TIME*5:
                    self.timeSkip = 0

                if up or down or left or right:
                    self.surface.fill((0, 0, 0, 0))
                    self.timeSkip += 1
                    self.animate(up, down, left, right)
                    self.go += 5

                if up:
                    self.y -= 5

                elif down:
                    self.y += 5

                elif left:
                    self.x -= 5

                elif right:
                    self.x += 5
            else:
                Player.mummyGo = 1
                self.go = 0

    
    def animate(self, up, down, left, right):
        img = ""
        if up:
            img = playerUp
        elif down:
            img = playerDown
        elif left:
            img = playerLeft
        elif right:
            img = playerRight

        if self.option == 0:
            self.surface.blit(img, (20, 20), (0, 0, 60, 60))
        if self.option == 1:
            self.surface.blit(img, (20, 20), (60, 0, 60, 60))
        if self.option == 2:
            self.surface.blit(img, (20, 20), (120, 0, 60, 60))
        if self.option == 3:
            self.surface.blit(img, (20, 20), (180, 0, 60, 60))
        if self.option == 4:
            self.surface.blit(img, (20, 20), (240, 0, 60, 60))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


class Mummy:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(mummyDown, (20, 20), (0, 0, 60, 60))
        self.timeSkip = 0
        self.option = 0

        self.go = 0

        self.locat = []
        self.keyRun = {"X":  self.x, "Y":  self.y}

    def update(self, up, down, left, right):

        if self.go < 100:

            if self.timeSkip <= TIME:  # 0 - 5
                self.option = 0
            elif self.timeSkip <= TIME*2:  # 6 - 10
                self.option = 1
            elif self.timeSkip <= TIME*3:  # 11 - 15
                self.option = 2
            elif self.timeSkip <= TIME*4:
                self.option = 3
            elif self.timeSkip <= TIME*5:
                self.option = 4

            elif self.timeSkip > TIME*5:
                self.timeSkip = 0

            if up or down or left or right:
                self.surface.fill((0, 0, 0, 0))
                self.timeSkip += 1
                self.animate(up, down, left, right)
                self.go += 5

            if up:
                self.y -= 5

            elif down:
                self.y += 5

            elif left:
                self.x -= 5

            elif right:
                self.x += 5
        else:
            self.go = 0
            Player.mummyGo += 1
            if Player.mummyGo == 3:
                Player.mummyGo = 0

    def run(self, keyPlayer, playerX, playerY):

        if self.x != self.keyRun['X']:
            # thay đổi x
            if self.x > self.keyRun['X']:
                self.update(False, False, True, False)
            else:
                self.update(False, False, False, True)

        elif self.y != self.keyRun['Y']:
            # thay đổi y
            if self.y > self.keyRun['Y']:
                self.update(True, False, False, False)

            else:
                self.update(False, True, False, False)
        else:
            keyMummy = getKey(self.x, self.y)

            lstFind = graph.findAllShortestPaths(keyMummy, keyPlayer)
       
            keyWall = getKey(wallX, wallY)
            keyWall2 = getKey(wallX2, wallY2)
            keyWall3 = getKey(wallX3, wallY3)
      
            # check wall dọc
            if keyMummy == keyWall or keyMummy == keyWall2 or keyMummy == keyWall3:
                if playerY == wallY or playerY == wallY2 or playerY == wallY3:
                    Player.mummyGo = 0
                else:
                    for item in lstFind:
                        if (item != keyWall - 1) or (keyMummy != keyWall2-1) or (keyMummy != keyWall3-1):
                            self.keyRun = getLocat(item)
            elif (keyMummy == keyWall-1) or (keyMummy == keyWall2-1) or (keyMummy == keyWall3-1):
                if playerY == wallY or playerY == wallY2 or playerY == wallY3:
                    Player.mummyGo = 0
                else:
                    for item in lstFind:
                        if (item != keyWall) or (keyMummy != keyWall2) or (keyMummy != keyWall3):
                            self.keyRun = getLocat(item)
            else:
                self.keyRun = getLocat(lstFind[0])

            # check wall ngang
            

    def animate(self, up, down, left, right):
        img = ""
        if up:
            img = mummyUp
        elif down:
            img = mummyDown
        elif left:
            img = mummyLeft
        elif right:
            img = mummyRight

        if self.option == 0:
            self.surface.blit(img, (20, 20), (0, 0, 60, 60))
        if self.option == 1:
            self.surface.blit(img, (20, 20), (60, 0, 60, 60))
        if self.option == 2:
            self.surface.blit(img, (20, 20), (120, 0, 60, 60))
        if self.option == 3:
            self.surface.blit(img, (20, 20), (180, 0, 60, 60))
        if self.option == 4:
            self.surface.blit(img, (20, 20), (240, 0, 60, 60))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


def main():
    player = Player()
    mummy = Mummy()

    up, down, left, right = False, False, False, False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True

        DISPLAYSURF.blit(surfaceMap, (0, 0))
        pygame.draw.rect(DISPLAYSURF, (0, 0, 255),
                         (wallX, wallY, wallW, wallH))
        
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0, 128),
                         (wallX2, wallY2, wallW2, wallH2))
        
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0, 128),
                         (wallX3, wallY3, wallW3, wallH3))
        
        DISPLAYSURF.blit(EXIT_IMAGE, (exit_x, exit_y))  # Vẽ lối exit
        DISPLAYSURF.blit(EXIT_IMAGE2, (exit_x2, exit_y2))
        DISPLAYSURF.blit(TRAP_IMAGE, (trap_x, trap_y))  # Vẽ bẫy

        player.draw()
        player.update(up, down, left, right)

        mummy.draw()

        if player.go == 0:
            up, down, left, right = False, False, False, False

        if Player.mummyGo > 0:
            keyPlayer = getKey(player.x, player.y)
            mummy.run(keyPlayer, player.x, player.y)

        # Kiểm tra va chạm giữa người chơi và xác ướp
        if player.x == mummy.x and player.y == mummy.y:
            DISPLAYSURF.blit(GAME_OVER_IMAGE, (0, 0))
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()

        # Kiểm tra điều kiện thắng
        win_coords = [(200, 570), (570, 200)]  # Thêm các toạ độ chiến thắng
        for win_x, win_y in win_coords:
            if abs(player.x - win_x) < 10 and abs(player.y - win_y) < 10:
                DISPLAYSURF.blit(VICTORY_IMAGE, (0, 0))
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()

        # Kiểm tra va chạm với bẫy
        if player.x == trap_x and player.y == trap_y:
            DISPLAYSURF.blit(GAME_OVER_IMAGE, (0, 0))
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()
            
        pygame.display.update()
        pygame.time.Clock().tick(60)
        
main()
