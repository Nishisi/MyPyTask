from controller import Controller

# Map の読み込み
gameMap = Controller.inputMap()

for i in range(len(gameMap)):
    print(gameMap[i])
