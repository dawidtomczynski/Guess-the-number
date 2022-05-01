from random import randint


def game():
    num_comp = randint(1, 100)
    while True:
        try:
            num_hero = int(input("Guess the number: "))
            if num_hero < num_comp:
                print("Too small!")
            elif num_hero > num_comp:
                print("Too big!")
            else:
                print("You win!")
                break
        except ValueError:
            print("Sorry, only integers are accepted.")


game()
