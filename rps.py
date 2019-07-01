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


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        plays = input("rock, paper, scissors\n")
        while plays != "rock" and plays != "paper" and plays != "scissors":
            print("invalid moves")
            plays = input("rock, paper, scissors\n")
        return plays


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if HumanPlayer.move is None:
            return "paper"
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class RockOnly(Player):
    def move(self):
        return "rock"


class Circler(Player):
    def __init__(self):
        Player.__init__(self)
        self.circler = "rock"

    def move(self):
        if self.circler == "rock":
            self.circler = "paper"
            return "paper"
        elif self.circler == "paper":
            self.circler = "scissors"
            return "scissors"
        else:
            self.circler = "rock"
            return "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_game(self):
        p1_score = 0
        p2_score = 0
        while True:
            rounds_choose = input("how many rounds do you want? \n")
            try:
                rounds_choose = int(rounds_choose)
                rounds_choose += 1
                break
            except ValueError:
                print("invalid input, please enter numbers only \n")
        print("Game start!")
        for round in range(1, rounds_choose):
            print(f"Round {round}: \n")
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            if ((move1 == 'rock' and move2 == 'scissors') or
                    (move1 == 'scissors' and move2 == 'paper') or
                    (move1 == 'paper' and move2 == 'rock')):
                print("Player 1 wins! \n")
                p1_score += 1
                print(f"player1 score is: {p1_score} ")
                print(f"player2 score is: {p2_score} ")
            elif move1 == move2:
                print("Tie!")
                print(f"player1 score is: {p1_score} ")
                print(f"player2 score is: {p2_score} ")
            else:
                print("Player 2 wins! \n")
                p2_score += 1
                print(f"player1 score is: {p1_score} ")
                print(f"player2 score is: {p2_score} ")
        print(f"player1 final score is: {p1_score} \n")
        print(f"player2 final score is: {p2_score} \n")
        if p1_score > p2_score:
            print("Player1 is the winner! \n")
        elif p1_score == p2_score:
            print("TIE!")
        else:
            print("Player2 is the winner! \n")
        print("Game over! \n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), Circler())
    game.play_game()
