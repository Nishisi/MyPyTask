class Map:
    """ Map用のクラス 壁とアイテム情報を保持する """

    # オリジナルのマップ
    originalMap = []
    # アイテムと壁マップ
    gameMap = []

    def get_original_map(self):
        return self.originalMap

    def get_game_map(self):
        return self.gameMap

    def create_map(self, dim):
        for i in range(len(dim)):
            maplist = []
            for j in dim[i]:
                if j == "#" or j == "o":
                    maplist.append(j)
                else:
                    maplist.append(" ")
            self.gameMap.append(maplist)

class Goal:
    """ Goal """
    def __init__(self, x, y):
        self.x = x
        self.y = y
