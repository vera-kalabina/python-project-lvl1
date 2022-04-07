#!/usr/bin/env python
from random import randint

INTRODUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    counter = 2
    num = int(num)
    while counter <= pow(num, 1 / 2):
        division_remainder = num % counter
        if num > 3 and division_remainder == 0:
            return('False')
        counter += 1
    return('True')


def question_and_result():
    question = randint(1, 250)
    result = 'yes' if is_prime(question) == 'True' else 'no'
    return question, result
