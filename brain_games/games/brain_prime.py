from random import randint 
from brain_games.games_core import make_game

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num):
    if num < 2:
        return True

    for i in range(2, num // 2):
        if num % i == 0:
            return False
        
    return True

def make_game_data():
    current_number = randint(1, 100)
    question = f'{current_number}'
    correct_answer = 'yes' if is_prime(current_number) else 'no'

    return (question, correct_answer)

def start_game():
    make_game(description, make_game_data)