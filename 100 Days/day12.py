import random
logo = """
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                      
"""

print(logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
    random_num = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess < random_num:
            print(f"Too low. Guess again.")
        elif user_guess > random_num:
            print(f"Too high. Guess again.")
        else:
            print(f"You got it! The answer was {random_num}")
        attempts -= 1
    print("You ran out of attempts. You lose.")

if difficulty == 'hard':
    attempts = 5
    random_num = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess < random_num:
            print(f"Too low. Guess again.")
        elif user_guess > random_num:
            print(f"Too high. Guess again.")
        else:
            print(f"You got it! The answer was {random_num}")
        attempts -= 1
    print("You ran out of attempts. You lose.")