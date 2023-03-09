from random import randint

class Die:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = None

    def roll(self):
        self.__value = randint(1, self.__sides)

    def get_sides(self):
        return self.__sides

    def get_value(self):
        return self.__value

    def __str__(self):
        return f"Value: {self.__value}; Sides: {self.__sides}"


def print_scores(player, pc, flag):
    if flag == 0:
        print(f"Player score: {player}")
    else:
        print(f"PC score: {pc}\nPlayer score: {player}")

if __name__ == "__main__":
    dice = [Die(6) for die in range(2)]
    game_on = True
    player_points = 0
    computer_points = 0
    while game_on:
        command = input("Do you want throw the dice or pass?(t/p)\n> ")
        if command.lower() == "t":
            for die in dice:
                die.roll()
                computer_points += die.get_value()
            for die in dice:
                die.roll()
                player_points += die.get_value()
            if player_points < 21:
                print_scores(player_points, computer_points, 0)

            elif player_points == 21:
                print_scores(player_points, computer_points, 1)
                print("You win!")
                input("---press enter to exit---")
                game_on = False
            
            elif player_points > 21:
                print_scores(player_points, computer_points, 1)
                print("You lose!")
                input("---press enter to exit---")
                game_on = False

        elif command.lower() == "p":
            if player_points == computer_points:
                print_scores(player_points, computer_points, 1)
                print("Draw!")
                input("---press enter to exit---")
                game_on = False
            elif player_points > computer_points:
                print_scores(player_points, computer_points, 1)
                print("You win!")
                input("---press enter to exit---")
                game_on = False
            else:
                print_scores(player_points, computer_points, 1)
                print("You lose!")
                input("---press enter to exit---")
                game_on = False