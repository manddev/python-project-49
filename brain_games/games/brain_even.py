from random import randint
from brain_games.games_core import make_game

RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100

def is_even(num):
    return num % 2 == 0

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def make_game_data():
    current_number = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    question = f'{current_number}'
    correct_answer = 'yes' if is_even(current_number) else 'no'

    return (question, correct_answer)

def start_game():
    make_game(DESCRIPTION, make_game_data)
    
        

        
        


