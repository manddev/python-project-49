from random import randint


MIN_VALUE = 1
MAX_VALUE = 100

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
        


DESCRIPTION = 'What is the result of the expression?'

def make_game_data():
    operations = ["*", "+", "-"]
    current_operation = operations[randint(0, len(operations) - 1)]
    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    question = f'{num1} {current_operation} {num2}'
    correct_answer = str(calculate_expression(num1, num2, current_operation))

    return (question, correct_answer)

def start_game():
    make_game(DESCRIPTION, make_game_data)