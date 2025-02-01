import prompt
from random import randint



greeting = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(num):
    return num % 2 == 0

rounds_count = 3

def make_game():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(greeting)

    
    current_round = 1
    corrects_count = 0
    
    while current_round <= rounds_count:
        current_number = randint(1, 100)
        print(f"Question: {current_number}")
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(current_number) else 'no'

        if user_answer == correct_answer:
            print('Correct!')
            current_round += 1
            corrects_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
        
        if corrects_count == 3:
                print(f'Congratulations, {name}!')
        

        
        


