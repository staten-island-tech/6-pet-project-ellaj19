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
        self.name = name
        self.__happiness = happiness
        self.__hunger = hunger
        self.__fear = fear
    def play(self):
        self.__happiness == 0
        question = input(f"do you want to play with {self.name}?")
        if question == "yes":
            self.__happiness += 10
        elif question == "no":
            self.__happiness -= 5
        else:
            print("invalid answer")
    def show_status(self):
        answer = input("do you want to see stats for day 1?")
        if answer == "yes":
            print(f"{self.name}'s happiness is at {self.__happiness}%. {self.name}'s hunger is at {self.__hunger}%. {self.name}'s fear is at {self.__fear}%.")
answer1 = input("what is your pet cat's name?")
print(f"hello, {answer1}")
cat = pet({answer1},50,50,25)
cat.play()
cat.show_status()