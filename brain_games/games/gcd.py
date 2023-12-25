import prompt
import random
import math


def find_correct_answer():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        result_gcd = math.gcd(number_1, number_2)
        print(f'Question: {number_1} {number_2}')
        user_answer = int(prompt.string('Your answer: '))
        if user_answer == result_gcd:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {result_gcd}.")
            print(f"Let's try again, {user_name}!")
            break
