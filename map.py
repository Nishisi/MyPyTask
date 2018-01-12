class Map:
    """ Map用のクラス 壁とアイテム情報を保持する """

    # オリジナルのマップ情報
    originalMap = []
    # アイテムと壁マップ情報
    gameMap = []

    # Getter -------------------
    def get_original_map(self):
        return self.originalMap

    def get_game_map(self):
        return self.gameMap

    # --------------------------

    # 配列を受け取りマップ情報作成する
    def create_map(self, dim):
        for i in range(len(dim)):
            maplist = []
            for j in dim[i]:
                if j == "#" or j == "o":
                    maplist.append(j)
                else:
                    maplist.append(" ")
            self.gameMap.append(maplist)

    # 座標を受け取り移動可能かどうか確認する 返り値はBool
    def check_map(self):
        pass

class Goal:
    """ Goal """
    def __init__(self, x, y):
        self.x = x
        self.y = y
