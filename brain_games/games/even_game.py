#!/usr/bin/env python
from random import randint


INTRODUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def question_and_result():
    question = randint(1, 100)
    result = 'yes' if is_even(question) is True else 'no'
    return question, result
