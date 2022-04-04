#!/usr/bin/env python
import prompt
from random import randint


def is_even(num):
    return num % 2 == 0


def run():
    number_of_attemps = 3
    attemp_number = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while attemp_number <= number_of_attemps:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = 'yes' if is_even(question) is True else 'no'
        if answer == result:
            print('Correct!')
            attemp_number = attemp_number + 1
            if attemp_number == 4:
                print(f'Congratulations, {name}!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'. \nLet's try again, {name}!"
            )
            break
    return
