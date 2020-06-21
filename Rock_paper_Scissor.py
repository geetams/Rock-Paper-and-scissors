#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# List of moves
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# Function to ask the user to restart the game
def restart_game():
    while True:
        print("Do you want to play again? Press [y/n]")
        restart = input(">")
        if(restart == 'y' or restart == 'Y'):
            game.play_game()
        elif (restart == 'n' or restart == 'N'):
            print("Thank you for playing")
            break
        else:
            print("Invalid input!!")
            break


# predefined function, to know the priority of one over the other
def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def get_input():
    Player_input = input('rock, paper, scissors? >')
    p_input = Player_input.lower()
    while p_input != 'rock' and p_input != 'paper' and p_input != 'scissors':
        print('Sorry try again')
        p_input = get_input()
        break

    return(p_input)


# player class with two attributes move and learn
# This fuction retuns defalt move as 'rock'
class Player:
    def move(self):
        return 'rock'

    def __init__(self):
        # initialization of the list for the move function
        self.my_move = moves
        # random choise for first round
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        # players moves are stored
        self.my_move = my_move
        self.their_move = their_move


# A class remembers the last move of opponet and playes in current move
class ReflectPlayer:

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return (random.choice(moves))
        else:
            return self.their_move


# Player 1--> as computer, chooses the moves randomely
class RandomPlayer(Player):

    def move(self):
        return (random.choice(moves))


# player2---> User, moves were inputed by the user
class HumanPlayer(Player):
    def move(self):
        Player_input = get_input()
        return (Player_input.lower())


# Class to chose a different move from the last round
class CyclePlayer(Player):
    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        return(my_move)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1                # p1- Computer player
        self.p2 = p2                # p2- User
        self.p1_win_cnt = 0         # variable to count plyer1 wins
        self.p2_win_cnt = 0         # variable to count plyer2 wins
        # self.tie_cnt = 0

# fuction to check the ststus of each player round
    def play_round(self):
        move1 = self.p1.move()  # record the moves of p1 & p2
        move2 = self.p2.move()
        print(f"\nYou played(P1)  : {move1} \nOpponent played(P2) : {move2}")
        if beats(move1, move2):
            self.p1_win_cnt += 1
            print("** PLAYER ONE WINS **")
        elif move1 == move2:
            self.p1_win_cnt = self.p1_win_cnt
            self.p2_win_cnt = self.p2_win_cnt
            print("** It's A TIE **")
        elif beats(move2, move1):
            self.p2_win_cnt += 1
            print("** PLAYER TWO WINS **")
        else:
            print("\nTHATS A MISTAKE!!")

        print(f"""Player1 Score: {self.p1_win_cnt} """
              f"""Player2 Score: {self.p2_win_cnt}\n\n""")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Game initiation function
    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            # function call to know the status of particular round
            self.play_round()
        # Function call to restart the game after 3 rounds
        restart_game()


if __name__ == '__main__':
    # player to is selected randomly
    player2 = random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()])
    # object creation of class game with two obj--player1, player2
    game = Game(HumanPlayer(), player2)
    # function call to start the game
    game.play_game()
