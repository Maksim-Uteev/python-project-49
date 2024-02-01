# Создать функцию, которая будет принимать параметром модуль игры
# (в скрипте можно вызывать функцию движка игры и передавать ей парметром модуль игры).
# В этой функции у нас будут:
# 1 все выводы на экран,
# 2 запрос имени пользователя,
# 3 правильного ответа,
# 4 цикл с раундами (внутри которого мы можем вызывать функции из модуля игры, который передали параметром).
# В модулях с играми нам нужно будет иметь одинаковый интерфейс (имена функций) чтобы в движке игры не нужно было писать особых условий под каждую игру.


def start_the_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.GAME_TASK)
    i = 0
    while i < 3:
        question, result = game_module.calculation()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
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
