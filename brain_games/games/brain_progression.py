from random import randint
from brain_games.games_core import make_game

description = 'What number is missing in the progression?'
progression_length = 10

def make_game_data():
    progression = []
    first_element = randint(1, 100)
    progression_step = randint(1, 100)
    progression.append(first_element)

    for i in range(0, progression_length - 1):
        next_element = progression[i] + progression_step
        progression.append(next_element)

    hidden_element_index = randint(1, progression_length - 1)
    correct_answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = '..'
    question = ' '.join(str(e) for e in progression)

    return (question, correct_answer)

def start_game():
    make_game(description, make_game_data)




