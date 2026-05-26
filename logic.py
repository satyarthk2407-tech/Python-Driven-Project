import random

def get_computer_choice():
    options = ['Stone', 'Paper', 'Scissors']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a tie!"

    if (
        (user_choice == 'Stone' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Stone') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win!"

    return "Computer wins!"