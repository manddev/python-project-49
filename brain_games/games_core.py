import prompt

ROUNDS_COUNT = 3


def run_game(description, make_game_data):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(description)

    for i in range(0, ROUNDS_COUNT):
        (question, correct_answer) = make_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )   
            return
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
