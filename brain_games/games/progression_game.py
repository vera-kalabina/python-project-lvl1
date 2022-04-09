from random import randint, randrange

INTRODUCTION = 'What number is missing in the proression?'
NUMBER_OF_TERMS = 10


def form_progression(first_operand, common_difference):
    progression = ''
    current_term = 0
    while current_term < NUMBER_OF_TERMS:
        progression += (f'{first_operand + common_difference * current_term} ')
        current_term += 1
    return progression


def question_and_result():
    first_operand = randint(1, 100)
    common_difference = randint(1, 100)
    last_operand = first_operand + (NUMBER_OF_TERMS - 1) * common_difference
    result = randrange(int(first_operand),
                       int(last_operand), int(common_difference))
    question = form_progression(first_operand,
                                common_difference).replace(str(result), '..', 1)
    return question, str(result)
