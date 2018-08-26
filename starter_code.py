#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

"""The RandomPlayer subclass chose moves at random"""

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

"""The HumanPlayer subclass allows users to chose their own moves"""
class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, Paper, or Scissors?")
            if choice.lower() in ['rock', 'paper', 'scissors']:
                return choice.lower()
"""The ReflectPlayer subclass copies its opponents last move"""
class ReflectPlayer(Player):
    def __init__(self):
        self.choice = random.choice(moves)
    def move(self):
        return self.choice
    def learn(self, my_move, their_move):
        self.choice = their_move

"""The CyclePlayer subclass cycles through the changes"""
class CyclePlayer(Player):
    def __init__(self):
        self.choice = 0
    def move(self):
        return moves[self.choice]
    def learn(self, my_move, their_move):
        if self.choice == 2:
            self.choice = 0
        else:
            self.choice += 1
    
        

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("Tie!")
        else:
            if beats(move1, move2):
                print("Player 1 wins!")
                self.p1_score += 1
            else:
                print("Player 2 wins!")
                self.p2_score += 1
        print(f"Player 1: {self.p1_score} Player 2: {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("You Win!")
            return True
        else:
            print("You Lose!")
            print("Game Over!")
            return False


if __name__ == '__main__':
    opponents = [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    human = HumanPlayer()
    rank = 0
    ranks = len(opponents)
    """Cycles through opponents until user loses or beats them. Uses the length
    of opponents as opposed to a static, so I can more easily add or remove players
    in the future"""
    while rank < ranks:
        print(f"Current opponent : {rank}")
        game = Game(human, opponents[rank])
        status = game.play_game()
        if  status:
            rank += 1
            if rank == ranks :
                print("You win it all!")
        else:
            rank = ranks
    print("That's all folks!")
            
