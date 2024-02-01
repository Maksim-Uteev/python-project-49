#!/usr/bin/env python3


from brain_games.engine import start_the_game
from brain_games.games import gcd


def main():
    start_the_game(gcd)


if __name__ == '__main__':
    main()
