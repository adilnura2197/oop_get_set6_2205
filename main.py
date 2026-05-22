class Futbolchi:
    def __init__(self, ism, gol):
        self.ism = ism
        self.__gol = gol

    def get_gol(self):
        return self.__gol

    def set_gol(self, gol):
        if gol >= 0:
            self.__gol = gol
            print("Gollar yangilandi")
        else:
            print("Xato qiymat")


f1 = Futbolchi("Ronaldo", 10)
print(f1.get_gol())
