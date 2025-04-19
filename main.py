"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Eva Pavlorková
email: pavlorkova.eva@seznam.cz
"""
from random import choice, sample

def print_line():
    print("-" * 47)

def greet_user():
    print("Hi, there!")
    print_line()
    print("I've generated a random 4 digit number for you.\
    \nLet's play a bulls and cows game.")
    print_line()
    print("Enter a number:")
    print_line()

def generate_number():
    numbers_int = list(range(10))
    numbers = [str(n) for n in numbers_int]
    number_1 = choice(numbers[1:])
    numbers.remove(number_1)
    next_numbers = sample(numbers, 3)
    return number_1 + "".join(next_numbers)

def get_guess():
    guess = input(">>>  ")
    print_line()
    return guess

def validate_guess(guess):
    return len(guess) == 4 \
        and guess.isnumeric() \
        and not guess.startswith("0") \
        and len(guess) == len(set(guess))
    
def bull_cow_numbers(guess, generated_number):
    bull_count = 0
    cow_count = 0
    x = 0
    for digit in guess:
        if digit == generated_number[x]:
            bull_count += 1
        elif digit in generated_number:
            cow_count += 1
        x += 1
    return bull_count, cow_count

def goodbye_text(guess_count):
    print("Correct, you've guessed the right number")
    print(f"in {guess_count} guesses!")
    print_line()
    print("That's amazing!")

def main():
    greet_user()
    generated_number = generate_number()
    guess = ""
    guess_count = 0

    while guess != generated_number:
        guess = get_guess()
        if validate_guess(guess):
            guess_count += 1
            bull_count, cow_count = bull_cow_numbers(guess, generated_number)
            print(f"{bull_count} bull{"s" if bull_count != 1 else ""}, "
                f"{cow_count} cow{"s" if cow_count != 1 else ""}")
            print_line()
        else:
            print("Wrong guess, try again.")
    
    goodbye_text(guess_count)

if __name__ == "__main__":
    main()