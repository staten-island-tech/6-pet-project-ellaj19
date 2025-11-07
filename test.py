class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
mia = Hero("mia",278,["fat, light brown hamster named gerald"])
mia.buy({"title": "poopy shoes", "atk": 5})
print(mia.__dict__)

class pet:
    def __init__(self, name, happiness, hunger, fear):
        self.name = input("what is your pet cat's name?")
        self.__happiness = happiness
        self.__hunger = hunger
        self.__fear = fear
    def play(self):
        self.__happiness == 0
        print(f"do you want to play with {self.name}?")
        if "yes":
            self.__happiness += 10
cat = pet("cat","cat",0,0)