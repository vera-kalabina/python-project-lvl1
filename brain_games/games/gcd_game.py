from random import randint
from math import gcd

INTRODUCTION = 'Find the greatest common divisor of given numbers.'


def question_and_result():
    first_operand, second_operand = randint(1, 100), randint(1, 100)
    question = (f'{first_operand} {second_operand}')
    result = gcd(first_operand, second_operand)
    return question, str(result)
