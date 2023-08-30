# Simple game in python

import random


def who_is_the_winner(human_choice, computer_choice):
    if (human_choice == 'rock' and computer_choice == 'scissors') or \
       (human_choice == 'scissors' and computer_choice == 'paper') or \
       (human_choice == 'paper' and computer_choice == 'rock'):

        return "human"

    elif human_choice == computer_choice:
        return "draw"

    else:
        return "computer"


def main():
    count_human = 0
    count_computer = 0
    choices = ['rock', 'paper', 'scissors']

    print("********** Rock---Paper---Scissors n**********\n")
    print("Welcome to the game\n")
    continue_game = True
    while continue_game:

        human_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        print('the human chooses: ', human_choice)

        computer_choice = random.choice(choices)
        print('the computer chooses: ', computer_choice)

        winner = who_is_the_winner(human_choice,computer_choice)

        if winner == "human":
            print("The winner is human")
            count_human += 1

        elif winner == "draw":
            print("What a draw game!")

        else:
            print("The computer is winner")
            count_computer += 1

        print("\nDo you want to continue the game?")
        answer = input()
        if answer == "no":
            continue_game = False
            print("\nThanks for playing!")
            print("The score of computer is:", count_computer)
            print("The score of human is :", count_human)

            print("\nOverall results:")
            if count_computer > count_human:
                print("Better luck next time!\n")
            elif count_computer == count_human:
                print("It is a draw\n")
            else:
                print("You win!\n")

            print("Have a nice day!")
            print("The End.")


if __name__ == "__main__":
    main()
