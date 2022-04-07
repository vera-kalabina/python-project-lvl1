#!/usr/bin/env python
from random import randint

introduction = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    count = 2
    num = int(num)
    while count <= pow(num, 1 / 2):
        simple = num % count
        if num > 3 and simple == 0:
            return('False')
        count += 1
    return('True')


def question_and_result():
    question = randint(1, 250)
    result = 'yes' if is_prime(question) == 'True' else 'no'
    return question, result
