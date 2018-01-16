class Player:
    """" Player class """

    # 初期座標を格納
    def __init__(self, y, x, name):
        self.name = name
        self.x = x
        self.y = y

    def get_coordinate(self):
        return self.y, self.x

    def set_coordinate(self, y, x):
        self.y, self.x = y, x

