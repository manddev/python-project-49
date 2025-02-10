from random import randint 


MIN_VALUE = 1
MAX_VALUE = 100

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
        
    return True

def make_game_data():
    current_number = randint(MIN_VALUE, MAX_VALUE )
    question = f'{current_number}'
    correct_answer = 'yes' if is_prime(current_number) else 'no'

    return (question, correct_answer)

