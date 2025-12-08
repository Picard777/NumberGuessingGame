import random  


def number_guessing_game():
    print("Welcome to the Number Guessing Game!") 
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 0

    print("\nDifficulty levels:")
    print("1.Easy (10 chances)")
    print("2.Meditum (5 chances)")
    print("3.Hard (3 chances)")

    difficulty = input("Please select difficulty (1, 2 or 3): ")
    if difficulty.isdigit():
        difficulty = int(difficulty)
        
    if difficulty == 1:
        max_attempts = 10
    elif difficulty == 2:
        max_attempts = 5
    elif difficulty == 3:
        max_attempts = 3
    else:
        print("Please enter a number from 1 to 3")
        return

    print(f"\nYou have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        guess_input = input("Enter your choice: ")
        if not guess_input.isdigit():
            print("Please enter a number!")

        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print('Too low! Try again.')
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The secret number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts")
            print("Do you want to try again?")
            print("1. Yes")
            print("2. No")
            again = int(input("Answer: "))
    
            if again == 1:
                number_guessing_game()
            elif again == 2:
                return
            
        print(f"Attempts left: {max_attempts - attempts}")
    print(f"\nOut of attempts! The number was {secret_number}")
    
    print("Do you want to try again?")
    print("1. Yes")
    print("2. No")
    again = int(input("Answer: "))
    
    if again == 1:
        number_guessing_game()
    elif again == 2:
        return
    

number_guessing_game()