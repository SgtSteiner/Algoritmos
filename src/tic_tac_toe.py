"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the
spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical,
or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a
game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to
return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
"""

from typing import List


def check_board(game_result: List[str]) -> str:
    # Horizontal
    for col in range(3):
        if all([game_result[col][row] == game_result[col][0] for row in range(1, 3)]):
            if game_result[col][0] != ".":
                return game_result[col][0]
    # Vertical
    for row in range(3):
        if all([game_result[col][row] == game_result[0][row] for col in range(1, 3)]):
            if game_result[0][row] != ".":
                return game_result[0][row]
    # Diagonal
    if all([game_result[i][i] == game_result[0][0] for i in range(3)]):
        if game_result[0][0] != ".":
            return game_result[0][0]
    if game_result[2][0] == game_result[1][1] == game_result[0][2]:
        if game_result[2][0] != ".":
            return game_result[2][0]

    return "D"


if __name__ == '__main__':
    print("Example:")
    print(check_board(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_board([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert check_board([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert check_board([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert check_board([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")