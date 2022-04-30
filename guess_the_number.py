from random import randint


def game():
    while not game == "You win!":
        num_comp = randint(1, 100)
        try:
            num_hero = int(input("Guess the number: "))
            if num_hero < num_comp:
                print("Too small!")
            elif num_hero > num_comp:
                print("Too big!")
            else:
                print("You win!")
        except ValueError:
            print("It's not a number!")


game()
