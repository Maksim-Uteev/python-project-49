import prompt


def start_the_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.GAME_TASK)
    i = 0
    while i < 3:
        question, result = game_module.calculation()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == result:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'")
            print(f"Let's try again, {user_name}!")
            break
