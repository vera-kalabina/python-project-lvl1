from random import randint, randrange

INTRODUCTION = 'What number is missing in the proression?'


def question_and_result():
    common_difference = randint(1, 10)
    first_operand = randint(1, 100)
    number_of_terms = 10
    current_term = 0
    tenth_operand = first_operand + 9 * common_difference
    question = ''
    while current_term < number_of_terms:
        question += (f'{first_operand + common_difference * current_term} ')
        current_term += 1
    result = randrange(int(first_operand),
                       int(tenth_operand), int(common_difference))
    question = str(question)
    question = question.replace(str(result), '..', 1)
    return question, str(result)
