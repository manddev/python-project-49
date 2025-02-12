from random import randint


RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10

def make_game_data():
    
    progression = []
    progression_initial_value = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    progression_step_value = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    progression = [str(progression_initial_value + i * progression_step_value) for i in range(PROGRESSION_LENGTH)]

    

    hidden_element_index = randint(1, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)

    return (question, correct_answer)
