import prompt


QUANTITY_OF_ROUNDS = 3


def run(game):
    round_number = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INTRODUCTION)
    while round_number <= QUANTITY_OF_ROUNDS:
        (question, result) = game.get_question_and_result()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            round_number = round_number + 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'. \nLet's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')
    return
