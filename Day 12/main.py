import random
from art import logo
print("Welcome to the number guessing game")

game_status = True

def play():
    print(logo)
    generated_number = random.randrange(0,101)
    #print((generated_number))
    print("I am thinking of a number between 0 to 100")
    game_level = input("What level do you want? easy or hard: ")

    if game_level == "easy":
        number_of_chances = 10
    elif game_level == "hard":
        number_of_chances = 5

    #print(number_of_chances)
   
    while number_of_chances != 0:
        user_guess = int(input("Make a guess? "))
        if user_guess < generated_number:
            print("Too low")
            number_of_chances -= 1
            print(f"You have {number_of_chances} remaining.\nGuess again!")
        elif user_guess > generated_number:
            print("Too high")
            number_of_chances -= 1
            print(f"You have {number_of_chances} remaining.ha\nGuess again!")
        elif user_guess == generated_number:
            print("You have guessed the right number!")
            number_of_chances = 0


play()

while game_status:
    should_continue = input("Do you want to go again? ")
    if should_continue == "y":
        play()
    else:
        print("Thank you for playing")
        game_status = False


    

    

