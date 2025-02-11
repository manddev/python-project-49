from random import randint 


RANDINT_MIN_VALUE = 1
RANDINT_MAX_VALUE = 100

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num // 2):
        if num % i == 0:
            return False
        
    return True

def make_game_data():
    current_number = randint(RANDINT_MIN_VALUE, RANDINT_MAX_VALUE)
    question = f'{current_number}'
    correct_answer = 'yes' if is_prime(current_number) else 'no'

    return (question, correct_answer)
