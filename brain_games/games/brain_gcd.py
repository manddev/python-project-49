import math
from random import randint
from brain_games.games_core import make_game


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def make_game_data():
    current_number1 = randint(1, 100)
    current_number2 = randint(1, 100)
    question = f'{current_number1} {current_number2}'
    correct_answer = str(math.gcd(current_number1, current_number2))

    return (question, correct_answer)

def start_game():
    make_game(DESCRIPTION, make_game_data)

