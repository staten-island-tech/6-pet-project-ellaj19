""" class Hero:
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
 """


class pet:
    def __init__(self, name, happiness, clean, hunger, fear, age):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
        self.clean = clean
        self.fear = fear
        self.age = age
    def play(self):
        self.__happiness == 0
        question = input(f"do you want to play with {answer1}?")
        if question == "yes":
            self.__happiness += 10
        elif question == "no":
            self.__happiness -= 10
        else:
            print("invalid answer")
    def feed(self):
        question1 = input(f"do you want to feed {answer1}?")
        if question1 == "yes":
            self.hunger -=10
            print("the hamster is getting bigger...")
        elif question1 == "no":
            self.hunger += 10 
            print("wrong choice")
        else:
            print("invalid answer")
    def wash(self):
        question2 = input(f"do you want to clean {answer1}?")
        if question2 == "yes":
            self.clean +=10
            print("thats not fur...")
        elif question2 == "no":
            self.clean -= 5 
            print("wash your hands")
        else:
            print("invalid answer")
    def secret(self):
        question3 = input("do you want to know a secret?")
        if question3 == "yes":
            self.__fear +=10
            print("wash the hamster")
            hamster.clean()
        elif question3 == "no":
            self.__clean -= 5 
            print("wash your hands")
        else:
            print("invalid answer")
    def show_status(self):
        self.age == 0
        answer = input("it's the end of the day. do you want to see stats?")
        if answer == "yes":
            self.age += 1
            print(f"{answer1}'s happiness is at {self.__happiness}%. {answer1}'s hunger is at {self.hunger}%. {answer1}'s fear is at {self.fear}%. {answer1}'s cleanliness is at {self.clean}%. {answer1}'s age is {self.age} days old")
        else:
            print(f"okay. {answer1} is sleeping.")
answer1 = input("what is your pet hamster's name?")
print(f"hello, {answer1}")
hamster = pet({answer1},50,50,25,25,0) 
print(f"welcome home, {answer1}! let's interact with the hamster.")
while hamster.age <= 24:
    hamster.play()
    hamster.feed()
    hamster.wash()
    hamster.show_status()
    if hamster.hunger <= -50:
        print("your hamster has died of obesity")
    if hamster.hunger >= 100:
        print(f"uh oh, {answer1} has died of hunger")
    if hamster.clean <= 0:
                print("your hamster passed away from its own odor")
    if hamster.fear >= 100:
                print("your hamster died of terror")
    if hamster.age == 24:
            print("your hamster passed away of old age")
    

