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
    def __init__(self, name, happiness, clean, hunger, fear):
        self.name = name
        self.__happiness = happiness
        self.__hunger = hunger
        self.__clean = clean
        self.__fear = fear
    def play(self):
        self.__happiness == 0
        question = input(f"do you want to play with {answer1}?")
        if question == "yes":
            self.__happiness += 10
        elif question == "no":
            self.__happiness -= 5
        else:
            print("invalid answer")
    def feed(self):
        question1 = input(f"do you want to feed {answer1}?")
        if question1 == "yes":
            self.__hunger -=10
            print("the hamster is getting bigger...")
        elif question1 == "no":
            self.__hunger += 5 
            print("wrong choice")
        else:
            print("invalid answer")
    def clean(self):
        question2 = input(f"do you want to clean {answer1}?")
        if question2 == "yes":
            self.__clean -=10
            print("thats not fur...")
        elif question2 == "no":
            self.__clean += 5 
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
        answer = input("it's the end of the day. do you want to see stats?")
        if answer == "yes":
            print(f"{self.name}'s happiness is at {self.__happiness}%. {self.name}'s hunger is at {self.__hunger}%. {self.name}'s fear is at {self.__fear}%.")
        else:
            print(f"okay. {answer1} is sleeping.")
answer1 = input("what is your pet hamster's name?")
print(f"hello, {answer1}")
hamster = pet({answer1},50,50,25,25) 
print(f"welcome home, {answer1}! let's interact with the hamster.")
hamster.play()
hamster.feed()
hamster.show_status()

def angryProfessor(k,a):
    a = []
    s = 0
    for i in range(a):
        if i <= 0:
            s += 1
            if s < k:
                print("yes")
            else: 
                print("no")

angryProfessor(3, [-2, -3, 1, 5])


