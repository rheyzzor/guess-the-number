import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()

