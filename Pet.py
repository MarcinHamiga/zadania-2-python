import os
import math

class Pet:
    def __init__(self):
        self._name = ""
        while len(self._name) < 3:
            self._name = input("Enter a name for your pet (min. 3 characters): ")
        self._hunger = 0
        self._tiredness = 0

    def _passage_of_time(self, food = 4, fun = 4):
        self._hunger += math.ceil(fun / 3)
        self._tiredness += math.ceil(food / 3)

    @property
    def mood(self):
        value = self._hunger + self._tiredness
        if value < 5:
            return "Happy"
        elif 5 <= value <= 10:
            return "Content"
        elif 11 <= value <= 15:
            return "Annoyed"
        elif value > 15:
            return "Furious"

    def talk(self):
        print(f"{self._name}'s mood is: {self.mood}")

    def eat(self, food = 4):
        self._passage_of_time(food=food)
        self._hunger -= food
        if self._hunger < 0:
            self._hunger = 0

    def play(self, fun = 4):
        self._passage_of_time(fun=fun)
        self._tiredness -= fun
        if self._tiredness < 0:
            self._tiredness = 0

    def __str__(self):
        return f"Name: {self._name}, hunger: {self._hunger}, tiredness: {self._tiredness}, mood: {self.mood}"

def main():
    game_on = True
    pet = Pet()
    food, fun = (4, 4)
    while game_on:
        print("What do you want to do with your pet?")
        command = input("1. Feed\n2. Play\n3. Talk\n4. Change the amount of food\n5. Change the amount of time spent playing\n6. Exit\n> ")
        if command.lower() == "1" or command.lower() == "feed":
            print("Your pet has eaten some good food.")
            pet.eat(food)
        elif command.lower() == "2" or command.lower() == "play":
            print("You played with your pet. It enjoyed it very much!")
            pet.play(fun)
        elif command.lower() == "4":
            try:
                food = int(input("New amount of food (must be more than 1): "))
                if food < 1:
                    food = 4
            except ValueError:
                food = 4
        elif command.lower() == "3" or command.lower() == "talk":
            pet.talk()
        elif command.lower() == "5":
            try:
                fun = int(input("New amount of fun (must be more than 1): "))
                if fun < 1:
                    fun = 4
            except ValueError:
                food = 4
        elif command.lower() == "6" or command.lower() == "exit":
            game_on = False
        elif command.lower() == "cheat_sheet":
            print(pet)
        input("---press enter to go back---")
        os.system("clear")


if __name__ == "__main__":
    main()
