from random import randint

RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_game_data():
    
    progression = []
    initial_value = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    step_value = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)

    for i in range(PROGRESSION_LENGTH):
        progression.append(str(initial_value + i * step_value))

    hidden_element_index = randint(0, PROGRESSION_LENGTH)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)

    return (question, correct_answer)


make_game_data()
