#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


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
            choice = input("rock, paper, or scissors? ")
            print("")
            if choice.lower() in moves:
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


"""The Game class contains the code for both playing a round,
or a game of rounds"""


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        if move1 == move2:
            print("Tie!\n")
        else:
            if beats(move1, move2):
                print("Player 1 wins!\n")
                self.p1_score += 1
            else:
                print("Player 2 wins!\n")
                self.p2_score += 1
        print(f"Player 1: {self.p1_score} Player 2: {self.p2_score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(5):
            print("*********")
            print(f"Round {round}:")
            print("*********\n")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("You Win!\n")
            return True
        else:
            print("You Lose!\n\nGame Over!\n")
            return False


"""The Tournament class plays several games against several players"""


class Tournament():
    def __init__(self, opponents):
        self.opponents = opponents
        self.human = HumanPlayer()
        self.rank = 0
        self.ranks = len(self.opponents)

    """Cycles through opponents until user loses or beats them. """
    def run_tournament(self):
        while self.rank < self.ranks:
            print("\n---------------")
            print(f"Current opponent : {self.rank}")
            print("-----------------\n")
            self.game = Game(self.human, self.opponents[self.rank])
            self.status = self.game.play_game()
            if self.status:
                self.rank += 1
                if self.rank == self.ranks:
                    print("You Win it All!\n")
            else:
                self.rank = self.ranks
        print("That's all folks!")


if __name__ == '__main__':
    tournament = Tournament([Player(), CyclePlayer(), ReflectPlayer(),
                             RandomPlayer()])
    tournament.run_tournament()
