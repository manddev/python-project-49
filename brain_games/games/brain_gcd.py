from random import randint
from brain_games.games_core import make_game

def get_greater_common_divisor(num1, num2):
    if (num2 > 0):
        divisor = num1 % num2
        return get_greater_common_divisor(num2, divisor)
    return abs(num1)

description = 'Find the greatest common divisor of given numbers.'

def make_game_data():
    current_number1 = randint(1, 100)
    current_number2 = randint(1, 100)
    question = f'{current_number1} {current_number2}'
    correct_answer = str(get_greater_common_divisor(current_number1, current_number2))

    return (question, correct_answer)

def start_game():
    make_game(description, make_game_data)

