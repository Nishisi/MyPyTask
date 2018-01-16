import copy
from map import Map
from player import Player
from enemy import EnemyA, EnemyB, EnemyC, EnemyD, EnemyE

class Controller:
    """ controller """

    mapInfo = Map()
    gameMap = []

    EnemyList = []
    player = None
    Items = 0

    # 外部ファイルからMap情報を読み込む
    def input_map(self):
        gmap = []

        f = open("map.txt")
        for line in f:
            gmap.append(line[:-1])
        f.close()

        # Mapインスタンスに設定する
        self.mapInfo.originalMap = gmap
        self.Items = self.mapInfo.create_map(gmap)

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
                    Controller.player = Player(i, j, "P")
                elif info[i][j] == "A":
                    Controller.EnemyList.append(EnemyA(i, j, "A"))
                elif info[i][j] == "B":
                    Controller.EnemyList.append(EnemyB(i, j, "B"))
                elif info[i][j] == "C":
                    Controller.EnemyList.append(EnemyC(i, j, "C"))
                elif info[i][j] == "D":
                    Controller.EnemyList.append(EnemyD(i, j, "D"))
                elif info[i][j] == "E":
                    Controller.EnemyList.append(EnemyE(i, j, "E"))
                else:
                    pass

    def play(self, num, order):
        self.printout(self.mapInfo.get_original_map())
        for i, o in zip(range(num), order):
            # print("================\n" + str(i+1) + " turn\n" + "================")
            # print("Press u(up) or d(down) or r(right) or l(left) or w(wait):", end="")
            # arrow = input()
            arrow = o
            self.input_check(arrow)
            game_map = copy.deepcopy(self.mapInfo.get_game_map())
            y, x = Controller.player.get_coordinate()
            # ここにマップ上に何があるかテェックする処理が必要
            if game_map[y][x] == "o":
                gmap = self.mapInfo.get_game_map()
                gmap[y][x] = " "
                self.Items = self.Items - 1
            elif game_map[y][x] == "G" and Items == 0:
                print("clear!!!!!!!!!!!!!!!!!!!!!!!!")
                return 0
            game_map[y][x] = Controller.player.name
            self.printout(game_map)

    # 入力のチェック(デバッグもしくは遊びよう)
    def input_check(self, signal):
        if signal == "w":
            # print("wait")
            pass
        elif signal == "r":
            # print("right")
            y, x = Controller.player.get_coordinate()
            if Controller.mapInfo.check_map(y, x + 1):
                Controller.player.set_coordinate(y, x + 1)
            else:
                exit(1)
            # print("Player(x , y):(", x, ",", y, ")")
        elif signal == "l":
            # print("left")
            y, x = Controller.player.get_coordinate()
            if Controller.mapInfo.check_map(y, x - 1):
                Controller.player.set_coordinate(y, x - 1)
            else:
                exit(1)
            # print("Player(x , y):(", x, ",", y, ")")
        elif signal == "u":
            # print("up")
            y, x = Controller.player.get_coordinate()
            if Controller.mapInfo.check_map(y - 1, x):
                Controller.player.set_coordinate(y - 1, x)
            else:
                exit(1)
            # print("Player(x , y):(", x, ",", y, ")")
        elif signal == "d":
            # print("down")
            y, x = Controller.player.get_coordinate()
            if Controller.mapInfo.check_map(y + 1, x):
                Controller.player.set_coordinate(y + 1, x)
            else:
                exit(1)
            # print("Player(x , y):(", x, ",", y, ")")
        else:
            pass

