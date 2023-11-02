# Project 1: AI Tic Tac Toe Algorithm Analysis

## Background Information
Tic-Tac-Toe is a game for two players: ‘X’ and ‘O’. The players are given a 3 x 3 board, where they alternate placing their symbols. The goal is to try and place 3 symbols in a line - whether it be vertically, horizontally, or diagonally. To create a computer player that plays optimally, we must keep two things in mind: what choices will lead the computer to a win, and which of those choices will do so faster? To do so, we must create an AI algorithm that will be able to handle the two.

The algorithm used is the Minimax Algorithm, which uses recursion to explore every possible course of action, and determines which would be the most optimal and efficient. This algorithm is very good at looking ahead and weighing out all its options. It’s important that our AI has knowledge of what’s to come for every decision it makes. The downfall of this algorithm is that, since it’s a recursive algorithm, it’s not the most time efficient. There MAY be an algorithm out there that has a faster run time.

## Instructions for Running the Code
To play Tic Tac Toe against a computer player, enter `python3 tic_tac_toe.py` at the command line. This will display a game board where the computer's moves are labeled as 'X'. Go ahead and pick cells to see if you can beat the computer!

## Explanation of its Structure
The following picture was really great help for me in understanding how the Minimax function works:

<p align="center">
<img width="214" alt="Screenshot 2023-11-02 at 1 54 29 PM" src="https://github.com/acast338/TicTacToe/assets/101237037/6bc4a772-ecb8-40bb-942c-dd906861e783">
</p>

In my implementation, I've calculated the scores using increments/decrements of 10 and -10, but everything else remains the same. We're given a tree that looks at the current state of the board, and determines all the possible choices it could make. The choices keep branching when: the game has yet to cease, the game has other options to choose from. When a branch finally reaches the end of the game, it will analyze which player has won the game, and return a values as a result:
* 10: the AI won
* 0: it was a tie
* -10: the human won

The AI evaluates the best choice by choosing the result that is worth the most. The ideal result to recieve is 10.

In the visual displayed above, the AI has three routes to take:
* Choosing cell 2 1: This route returns a 10 off the first recursive call, so this route ensures a quick win for the AI.
* Choosing cell 2 3: Leaves the choice up to the person where they can:
  * Choose cell 2 1: Which forces the AI to choose cell 3 2, resulting in a tie (return 0).
  * Choose cell 3 2: Which forces the AI to choose cell 2 1, resulting in a win for the AI (return 10).
* Choosing cell 3 2: Leaves the choice up to the person where they can:
  * Choose cell 2 1: Which forces the AI to choose cell 3 2, resulting in a tie (return 0).
  * Choose cell 2 3: Which results in the person winning (return -10).
