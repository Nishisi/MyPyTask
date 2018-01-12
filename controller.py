from map import Map
from player import Player
from enemy import EnemyA, EnemyB, EnemyC, EnemyD, EnemyE

class Controller:
    """ controller """

    mapInfo = Map()
    gameMap = []

    EnemyList = []
    player = None

    # 外部ファイルからMap情報を読み込む
    def input_map(self):
        gmap = []

        f = open("map.txt")
        for line in f:
            gmap.append(line[:-1])
        f.close()

        # Mapインスタンスに設定する
        self.mapInfo.originalMap = gmap
        self.mapInfo.create_map(gmap)

    # マップを出力する
    def printout(self, info):
        for i in info:
            for j in i:
                print(j, end='')
            print("")

    # マップの敵情報とプレイヤー情報を取得する
    def take_map_info(self):
        info = self.mapInfo.get_original_map()
        for i in range(len(info)):
            for j in range(len(info[i])):
                if info[i][j] == "S":
                    Controller.player = Player(i, j)
                elif info[i][j] == "A":
                    Controller.EnemyList.append(EnemyA(i, j))
                elif info[i][j] == "B":
                    Controller.EnemyList.append(EnemyB(i, j))
                elif info[i][j] == "C":
                    Controller.EnemyList.append(EnemyC(i, j))
                elif info[i][j] == "D":
                    Controller.EnemyList.append(EnemyD(i, j))
                elif info[i][j] == "E":
                    Controller.EnemyList.append(EnemyE(i, j))
                else:
                    pass

    def play(self, num):
        self.printout(self.mapInfo.get_original_map())
        for i in range(num):
            print("================\n" + str(i+1) + " turn\n" + "================")
            print("Press u(up) or d(down) or r(right) or l(left) or w(wait):", end="")
            arrow = input()
            self.input_check(arrow)
            self.printout(self.mapInfo.get_game_map())

    def input_check(self, signal):
        if signal == "w":
            print("wait")
            pass
        elif signal == "r":
            print("right")
            pass
        elif signal == "l":
            print("left")
            pass
        elif signal == "u":
            print("up")
            pass
        elif signal == "d":
            print("down")
            pass
        else:
            pass

