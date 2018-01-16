import itertools
from controller import Controller

controller = Controller()

# Map の読み込み
controller.input_map()
# Player and 敵の情報を取得
controller.take_map_info()

order = 'wlrud'
n = 10
seq = []
for i in order:
    for j in range(n):
        seq.append(i)
print(seq)

# ゲーム開始
oh = list(itertools.permutations(seq, 3))
for i in oh:
    controller.play(10, oh)

