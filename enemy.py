class Enemy:
    """ Enemy class """

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y

    def getCoordinate(self):
        return self.x, self.y

    def setCoordinate(self, x, y):
        self.x, self.y = x, y



class EnemyA(Enemy):
    def get(self):
        pass

class EnemyB(Enemy):
    def get(self):
        pass

class EnemyC(Enemy):
    def get(self):
        pass

class EnemyD(Enemy):
    def get(self):
        pass

class EnemyE(Enemy):
    def get(self):
        pass


