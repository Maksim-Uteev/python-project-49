import prompt


GAME_ROUND = 3


def start_the_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game_module.GAME_TASK)

    for _ in range(GAME_ROUND):
        question, correct_answer = game_module.get_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {user_name}!")
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
