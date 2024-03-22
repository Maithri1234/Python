import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_result(user_choice, computer_choice, winner):
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"The {winner} wins!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        if not play_again():
            print("Thanks for playing!")
            break

play_game()
