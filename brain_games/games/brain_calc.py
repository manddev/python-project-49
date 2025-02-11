from random import randint, choice


RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100

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
    current_operation = choice(operations)
    num1 = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    num2 = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    question = f'{num1} {current_operation} {num2}'
    correct_answer = str(calculate_expression(num1, num2, current_operation))

    return (question, correct_answer)

