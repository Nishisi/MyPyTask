class Controller:
    """ controller """

    def inputMap():
        # Map の読み込み
        Gmap = []
        f = open("map.txt")

        for line in f:
            Gmap.append(line[:-1])

        f.close()

        return Gmap
