class Player:
    """" Player class """

    # 初期座標を格納
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Player の座標を移動させる
    def move(self, signal):
        if signal == "w":
            pass
        elif signal == "r":
            pass
        elif signal == "l":
            pass
        elif signal == "u":
            pass
        elif signal == "d":
            pass
        else:
            pass

    # 移動先に障害物がないか確認する
    def check_map(self):
        pass

