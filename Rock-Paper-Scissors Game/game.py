import random

# Global score variables
user_score = 0
computer_score = 0

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    global user_score, computer_score
    
    while True:
        print("Choose: rock, paper, or scissors")
        user_choice = input().lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores - You: {user_score} | Computer: {computer_score}")
        
        print('\n')
        break

# Start the game
while True:
    # Reset scores for a new game
    user_score = 0 
    computer_score = 0
    
    #The three turn game
    print('\n')
    print("Starting a new game!")
    for turn in range(3):
        print(f"Turn {turn + 1}")
        play_game()
        
    #Final Result
    print("Final Result : ")
    if (user_score > computer_score):
        print('You Won the Game')
    elif(user_score < computer_score):
        print('You Lose the Game')
    else:
        print('The Game is a Tie')
    
    #Play Again Option
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
