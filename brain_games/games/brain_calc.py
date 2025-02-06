from random import randint
from brain_games.games_core import make_game


def calculate_expression(num1, num2, operation):
    match operation:
        case '*':
            return num1 * num2
        case "-":
            return num1 - num2
        case "+":
            return num1 + num2
        case _:
            return None
        


description = 'What is the result of the expression?'

def make_game_data():
    operations = ['*', "+", "-"]
    current_operation = operations[randint(0, len(operations) - 1)]
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    question = f'{num1} {current_operation} {num2}'
    correct_answer = str(calculate_expression(num1, num2, current_operation))

    return (question, correct_answer)

def start_game():
    make_game(description, make_game_data)