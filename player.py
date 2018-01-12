class Player:
    """" Player class """

    # 初期座標を格納
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next_x = 0
        self.next_y = 0

