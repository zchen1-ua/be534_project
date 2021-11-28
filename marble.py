#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-11-25
Purpose: The marble fame (guess even or odd)
"""

import time
import argparse
import random

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--player',
                        help='Player\'s name',
                        metavar='name',
                        type=str,
                        default='Player')

    parser.add_argument('-n',
                        '--number',
                        help='Number of marbles for each player',
                        metavar='number',
                        type=int,
                        choices=[10, 15, 20, 25],
                        default='20')

    parser.add_argument('-f',
                        '--first',
                        help='Choose to guess first',
                        action='store_true')

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    n_me = n_op = args.number

    print(f'Welcome to the game, {args.player}\n')
    time.sleep(1)

    if args.first:
        while n_me > 0  and n_op > 0:
            n_op, n_me = me_guess(n_op, n_me)
            if n_me > 0  and n_op > 0:
                n_op, n_me = op_guess(n_op, n_me)
    else:
        while n_me > 0  and n_op > 0:
            n_op, n_me = op_guess(n_op, n_me)
            if n_me > 0  and n_op > 0:
                n_op, n_me = me_guess(n_op, n_me)

    if n_op <= 0:
        print(f'Congratuations {args.player}! You won the game!')
    elif n_me <= 0:
        print(f'Unfortunately, {args.player}, you lost the game.')


# --------------------------------------------------
def op_guess(n_op: int, n_me: int):

    print(f'You have {n_me} marbles left')
    time.sleep(1)
    print(f'Your opponent has {n_op} marbles left\n')
    time.sleep(1)

    bet = input(f'Select a number between 0 and {n_me}: ')
    time.sleep(1)
    bet = int(bet)
    guess = random.choice(['odd', 'even'])

    if (guess == "odd") == is_odd(bet):
        n_op += bet
        n_me -= bet
        print(f'Your opponent guessed it right! You lost {bet} marbles.')

    else:
        n_op -= bet
        n_me += bet
        print(f'Your opponent guessed it wrong! You won {bet} marbles.')
    
    return (n_op, n_me)

    
# --------------------------------------------------
def me_guess(n_op: int, n_me: int):

    print(f'You have {n_me} marbles left')
    time.sleep(1)
    print(f'Your opponent has {n_op} marbles left\n')
    time.sleep(1)

    bet = random.choice(range(0, n_op))
    guess = input('Make a guess between even and odd : ')
    time.sleep(1)

    if guess_right(bet, guess):
        n_me += bet
        n_op -= bet
        print(f'You guessed it right! You won {bet} marbles')
    else:
        n_op += bet
        n_me -= bet
        print(f'You guessed it wrong! You lost {bet} marbles')

    return (n_op, n_me)


# --------------------------------------------------
def guess_right(bet: int, guess: str):
    if is_odd(bet) and (guess == "odd"):
        return True
    else:
        return False
    

# --------------------------------------------------
def is_odd(num: int):
    if (num % 2) == 1:
        return True
    else:
        return False


# --------------------------------------------------
if __name__ == '__main__':
    main()
