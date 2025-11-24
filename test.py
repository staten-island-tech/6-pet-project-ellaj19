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

""" """ 
class pet:
    def __init__(self, name, happiness, clean, hunger, fear, age):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
        self.clean = clean
        self.fear = fear
        self.age = age
    def play(self):
        question = input(f"do you want to play with {answer1}? yes/no")
        if question == "yes":
            self.__happiness += 10
            self.hunger +=5
        elif question == "no":
            self.__happiness -= 10
        elif self.__happiness == 100:
             print("great job taking care of your meal")
        else:
            print("invalid answer")
    def feed(self):
        question1 = input(f"do you want to feed {answer1}? yes/no")
        if question1 == "yes":
            self.hunger -=10
            print("the hamster is getting bigger...")
        elif question1 == "no":
            self.hunger += 10 
            print("wrong choice")
        else:
            print("invalid answer")
    def wash(self):
        question2 = input(f"do you want to clean {answer1}? yes/no")
        if question2 == "yes":
            self.clean +=10
            print("thats not fur...")
        elif question2 == "no":
            self.clean -= 5 
            print("wash your hands")
        elif self.__happiness == 100:
             print("great job taking care of your meal")
        else:
            print("invalid answer")
    def show_status(self):
        answer = input("it's the end of the day. do you want to see stats? yes/no")
        if answer == "yes":
            self.age += 1
            print(f"{answer1}'s happiness is at {self.__happiness}%. {answer1}'s hunger is at {self.hunger}%. {answer1}'s fear is at {self.fear}%. {answer1}'s cleanliness is at {self.clean}%. {answer1}'s age is {self.age} days old")
        else:
            self.age += 1
            print(f"okay. {answer1} is sleeping.")
answer1 = input("what is your pet hamster's name?")
print(f"hello, {answer1}")
hamster = pet({answer1},50,50,25,25,12) 
print(f"welcome home, {answer1}! let's interact with the hamster.")
while hamster.age <= 24:
    hamster.play()
    hamster.feed()
    hamster.wash()
    hamster.show_status()
    if hamster.hunger <= -50:
        print("your hamster has died of obesity")
        break
    elif hamster.hunger >= 100:
        print(f"uh oh, {answer1} has died of hunger")
        break
    elif hamster.clean <= 0:
        print("your hamster passed away from its own odor")
        break
    elif hamster.fear >= 100:
        print("your hamster died of terror")
        break
    elif hamster.age == 24:
        print("your hamster passed away of old age")
        break

""" def isValid():
    email = input("what is your email?")
    password = input("what is your password?")
    if "@" not in email:
        return "not valid email"
    if any(char.isupper() for char in password) == False:
      return "invalid password: needs at least 1 uppercase letter"
    elif any(char.isdigit() for char in password) == False:
       return "invalid password: needs at least 1 number"
    elif any(len(password) >= 8 for char in password) == False:
       return "invalid password: needs to be at least 8 characters long"
    return{'email':email, 'password':password}

print(isValid()) """

def secret(self):
        question3 = input("do you want to know a secret?")
        if question3 == "yes":
            self.fear +=10
            print("wash the hamster")
            hamster.wash()
        elif question3 == "no":
            self.clean -= 5 
            print("wash your hands")
        else:
            print("invalid answer")




    
  