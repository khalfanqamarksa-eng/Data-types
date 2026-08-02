class World():
    def __init__(self,  continent, capital):
        self.continent = continent
        self.capital = capital
    def print(self):
        pass
class Pakistan(World):
    def print(self):
        print("Pakistan's capital is", self.capital)
class China(World):
    def print(self):
        print("China's continent is", self.continent)
Pak = Pakistan("Asia", "Islamabad")
China= China("Asia", "Beijing")
Pak.print()
China.print()