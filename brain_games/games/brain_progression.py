from random import randint
from brain_games.games_core import make_game

MIN_VALUE = 1
MAX_VALUE = 100

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10

def make_game_data():
    
    progression = []
    first_element = randint(MIN_VALUE, MAX_VALUE)
    progression_step = randint(MIN_VALUE, MAX_VALUE)
    progression.append(first_element)

    for i in range(0, PROGRESSION_LENGTH - 1):
        next_element = progression[i] + progression_step
        progression.append(next_element)

    hidden_element_index = randint(1, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = '..'
    question = ' '.join(str(e) for e in progression)

    return (question, correct_answer)

def start_game():
    make_game(DESCRIPTION, make_game_data)




