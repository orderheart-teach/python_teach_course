import random


number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("welcome to the guess number game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
print("Good luck!")

while attempts < max_attempts:
    try:
        guess = int(input("Please enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    attempts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've run out of attempts. The number was {number}.")
    
print("Game over!")