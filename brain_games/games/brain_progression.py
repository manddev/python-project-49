from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
PROGRESSION_LENGTH = 10

DESCRIPTION = 'What number is missing in the progression?'


def make_game_data():
    
    progression = []
    initial_value = randint(MIN_NUMBER, MAX_NUMBER)
    step_value = randint(MIN_NUMBER, MAX_NUMBER)

    for i in range(PROGRESSION_LENGTH):
        progression.append(str(initial_value + i * step_value))

    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)

    return (question, correct_answer)
