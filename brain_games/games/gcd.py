import random
import math

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def calculation():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    result = str(math.gcd(number_1, number_2))
    return question, result
