class computer:
    def __init__(self):
        self.__max_price= 900
    def sell(self):
        print ("Selling price: {}".format(self.__max_price))
    def setMaxPrice(self, price):
        self.__max_price= price
obj = computer()
obj.sell()

obj.__max_price = 1000
obj.sell()

obj.setMaxPrice(1000)
obj.sell()