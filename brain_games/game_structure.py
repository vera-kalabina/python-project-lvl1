import prompt


def run(game):
    number_of_attemps = 3
    attemp_number = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.introduction)
    while attemp_number <= number_of_attemps:
        (question, result) = game.question_and_result()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
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