# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:15:56 2019
Rock, Paper, Scissors
@author: Adam ponting's pc
"""
def movechecker(move1, move2):
    """
    checks that both moves are correct (rock, paper or scissors)
    """
    moves = ["rock","paper","scissors"]
    if move1 not in moves or move2 not in moves:
        return False
    return True

def game(player1, player2, rounds):
    scorep1 = 0
    scorep2 = 0
    while rounds > 0:
        move1 = input("Enter Player 1's move: rock, paper or scissors (nocaps): ")
        move2 = input("Enter Player 2's move: rock, paper or scissors (nocaps): ")
        if movechecker(move1, move2) == True:
            if move1 == move2:
                print("draw!")
            elif move1 == "paper" and move2 == "rock":
                scorep1 += 1
                print(player1 + " scores!")
            elif move1 == "rock" and move2 == "scissors":
                scorep1 += 1
                print(player1 + " scores!")
            elif move1 == "scissors" and move2 == "paper":
                scorep1 += 1
                print(player1 + " scores!")
            else:
                scorep2 += 1
                print(player2 + " scores!")
        else:
            print("One of ya messed up")
        rounds -= 1
    if scorep1 > scorep2:
        print( "\n" + player1 + " is the winner!!")
    elif scorep1 < scorep2:
        print("\n" + player2 + " is the winner!!")
    else:
        print("\n" + player1 + " and " + player2 + " have drawn!!")

## Main Sequence
player1 = input("Enter Player 1's name: ")
player2 = input("Enter Player 2's name: ")
rounds = int(input("Enter the number of rounds you wish to play: "))
game(player1, player2, rounds)  
