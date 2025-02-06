from random import randint
from brain_games.games_core import make_game



def is_even(num):
    return num % 2 == 0

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def make_game_data():
    current_number = randint(1, 100)
    question = f'{current_number}'
    correct_answer = 'yes' if is_even(current_number) else 'no'

    return (question, correct_answer)

def start_game():
    make_game(description, make_game_data)
    
        

        
        


