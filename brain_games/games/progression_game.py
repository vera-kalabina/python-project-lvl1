from random import randint, randrange

INTRODUCTION = 'What number is missing in the proression?'
NUMBER_OF_ELEMENTS = 10


def create_progression(first_operand, last_operand, common_difference):
    progression = ''
    for i in range(first_operand,last_operand+1,common_difference):
        progression += str(i) + ' '
    return progression


def get_question_and_result():
    first_operand = randint(1, 100)
    common_difference = randint(1, 100)
    last_operand = first_operand + (NUMBER_OF_ELEMENTS - 1) * common_difference
    result = randrange(int(first_operand),
                       int(last_operand), int(common_difference))
    progression = create_progression(first_operand, last_operand,
                                    common_difference)
    question = progression.replace(str(result), '..', 1)
    return question, str(result)
