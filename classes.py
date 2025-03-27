class Separate:
    def __init__(self, list):
        data = list.split(";")
        self.index = int(data[0])
        self.artist = data[1]
        self.title = data[2]
        self.length = data[3]