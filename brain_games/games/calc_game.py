from random import randint, choice

INTRODUCTION = 'What is the result of the expression?'


def get_question_and_result():
    first_operand, second_operand = randint(0, 100), randint(0, 100)
    operator = choice('+-*')
    question = (f'{first_operand} {operator} {second_operand}')
    if operator == '+':
        result = first_operand + second_operand
    elif operator == '-':
        result = first_operand - second_operand
    elif operator == '*':
        result = first_operand * second_operand
    return question, str(result)
