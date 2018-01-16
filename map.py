class Map:
    """ Map用のクラス 壁とアイテム情報を保持する """

    # オリジナルのマップ情報(読み込んだままのマップ)
    originalMap = []
    # アイテムと壁マップ情報(書き換えはおきない)
    gameMap = []

    # Getter -------------------
    def get_original_map(self):
        return self.originalMap

    def get_game_map(self):
        return self.gameMap

    # --------------------------

    # 配列を受け取りマップ情報作成する. アイテムの数を返す
    def create_map(self, dim):
        items = 0
        for i in range(len(dim)):
            maplist = []
            for j in dim[i]:
                if j == "#" or j == "G":
                    maplist.append(j)
                elif j == "o":
                    items = items + 1
                    maplist.append(j)
                else:
                    maplist.append(" ")
            self.gameMap.append(maplist)
        return items

    # 敵などの情報を受け取り、マップに描画するメソッド
    def draw_info(self):
        pass

    # 座標を受け取り移動可能かどうか確認する 返り値はBool
    def check_map(self, x, y):
        if self.gameMap[x][y] != "#":
            return True
        else:
            return False
        pass
