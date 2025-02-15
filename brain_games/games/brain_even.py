from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def make_game_data():
    current_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{current_number}'
    correct_answer = 'yes' if is_even(current_number) else 'no'

    return (question, correct_answer)

    
        

        
        


