import random

def computer_guess_number():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 500, and I'll try to guess it.")
    
    lower_bound = 1
    upper_bound = 500
    guess = none 
    
    while True:
        guess = random.randint(lower_bound, upper_bound)
        print("Is your number higher, lower, or equal to", guess, "?")
        user_input = input("Enter 'H' for higher, 'L' for lower, or 'C' for correct: ").lower()
        
        if user_input == 'c':
            print("Hooray! I guessed your number, it's", guess, "!")
            break
        elif user_input == 'h':
            lower_bound = guess + 1
        elif user_input == 'l':
            upper_bound = guess - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

computer_guess_number()
