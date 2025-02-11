import math
from random import randint


RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def make_game_data():
    current_number1 = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    current_number2 = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    question = f'{current_number1} {current_number2}'
    correct_answer = str(math.gcd(current_number1, current_number2))

    return (question, correct_answer)
