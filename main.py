from controller import Controller

controller = Controller()

# Map の読み込み
controller.input_map()

# Player and 敵の情報を取得
controller.take_map_info()

# ゲーム開始
controller.play(50)

