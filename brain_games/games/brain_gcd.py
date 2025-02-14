import math
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_game_data():
    current_number1 = randint(MIN_NUMBER, MAX_NUMBER)
    current_number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{current_number1} {current_number2}'
    correct_answer = str(math.gcd(current_number1, current_number2))

    return (question, correct_answer)
