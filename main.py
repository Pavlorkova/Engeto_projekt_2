"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Eva Pavlorková
email: pavlorkova.eva@seznam.cz
"""
from random import choice, sample

print("Hi, there!")
line = "-" * 47
print(line)
print("I've generated a random 4 digit number for you.\
\nLet's play a bulls and cows game.")
print(line)
print("Enter a number:")
print(line)

numbers_int = list(range(10))
numbers = [str(n) for n in numbers_int]
number_1 = choice(numbers[1:])
numbers.remove(number_1)
next_numbers = sample(numbers, 3)
generated_number = number_1 + "".join(next_numbers)

guess = 0
guess_count = 0
while guess != generated_number:
    bull_count = 0
    cow_count = 0
    guess = input(">>>  ")
    print(line)
    if len(guess) == 4 and guess.isnumeric() and not guess.startswith("0") \
        and len(guess) == len(set(guess)):
        guess_count += 1
        x = 0
        for digit in guess:
            if digit == generated_number[x]:
                bull_count += 1
            elif digit in generated_number:
                cow_count += 1
            x += 1
        print(f"{bull_count} bull{"s" if bull_count != 1 else ""}, "
              f"{cow_count} cow{"s" if cow_count != 1 else ""}")
        print(line)
    else:
        print("Wrong guess, try again.")

print(f"Correct, you've guessed the right number in {guess_count} guesses!")
print(line) 
print("That's amazing!")
