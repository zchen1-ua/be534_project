# Marble Game (Final Project for BE534)

###  Overview

This is my final project for the BE534 class. It's inspired by the marble game in the TV show "Squid Game" Season 1 Episode 6.

The objective of the game is to collect all the marbles. This game involves two players. Each player begins with the same number of marbles (can use the -n argument to choose from 10/15/20/25). They have to pick some number of marbles in their fist and ask the opposite player to guess whether he/she has an odd or even number of marbles. If the guess is correct then the player who is playing has to return those marbles to the opposite player, if the guess is wrong then the opposite player has to give that number of marbles to the player. Both of them will get an alternative turn to play. At the end, whoever has all the marbles will be the winner.

### Usage

** The program uses as input **

* Player's name `(-p, --player)`
* The starting number of marbles for both players `(-n, --number)`
* A boolean flag to choose to guess first '(-f, --first)'

When run with the `-h|--help` flags, it prints a help message:

```
usage: marble.py [-h] [-p name] [-n number] [-f]

The marble game (guess even or odd)

optional arguments:
  -h, --help            show this help message and exit
  -p name, --player name
                        Player's name (default: Player)
  -n number, --number number
                        Number of marbles for each player (default: 20)
  -f, --first           Choose to guess first (default: False)
```
