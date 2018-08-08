"""
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns. You should design your code to find
how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

"""
ROWS = "12345678"
COLS = "abcdefgh"


def safe_pawns(pawns: set) -> int:
    pawns_count = 0
    for pawn in pawns:
        pawn_row = ROWS.find(pawn[1])
        pawn_col = COLS.find(pawn[0])
        if pawn_row > 0:
            if pawn_col - 1 >= 0:
                if (COLS[pawn_col - 1] + ROWS[pawn_row - 1]) in pawns:
                    pawns_count += 1
                    continue
            if pawn_col + 1 <= 7:
                if (COLS[pawn_col + 1] + ROWS[pawn_row - 1]) in pawns:
                    pawns_count += 1
    return pawns_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")