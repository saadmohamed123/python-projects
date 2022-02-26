import random

try:
    computer_guess = ["rock", "paper", "sisor"]

    rock = "rock"
    sisor = "sisor"
    paper = "paper"

    def game_processer(input):
        if input == rock or paper or sisor:
            return random.choice(computer_guess)

# choose wether rock paper or sisor

    print(game_processer(rock))

except:
    print("invalid input")
