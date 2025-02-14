from random import choice, randint

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = 'What is the result of the expression?'


def calculate_expression(num1, num2, operation):
    match operation:
        case '*':
            return num1 * num2
        case '-':
            return num1 - num2
        case '+':
            return num1 + num2
        case _:
            return None


def make_game_data():
    operations = ['*', '+', '-']
    current_operation = choice(operations)
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num1} {current_operation} {num2}'
    correct_answer = str(calculate_expression(num1, num2, current_operation))

    return (question, correct_answer)

