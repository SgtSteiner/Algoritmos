"""
Problem #134 Flying Text Screensaver

http://www.codeabbey.com/index/task_view/flying-text-screensaver

This useless program is sometimes proposed by school teachers: using extended console functions for positioning
cursor and printing text in any possible position on the screen, pupils are to create effect of the flying text
with the given string.

Text should move diagonally with the constant speed (for example, 3 cells per second) and bounce from the borders.
Bouncing means that when the string reaches last or first line, it changes the vertical direction - and when its end
or start touches last or first column respectively - it changes the horizontal direction.

Play with the demo above to get better idea of how it works. Or, perhaps, write such program using what means your
programming language offer - and see it in action.

Your task now is to track the path of the flying text.

Input data will contain Width and Height of the imaginary screen and the Length of text string.
Answer should dump pairs of coordinates X and Y of the beginning of the text for first 100 steps
(spaces should be used to separate values in the pair and pairs themselves) - i.e. 202 integers in total
(including coordinates of the starting position).

Coordinate system of the screen usually has the (0, 0) in the left top corner.

Example:

input data:
9 3 4

answer:
0 0 1 1 2 2 3 1 4 0 5 1 4 2 3 1 2 0 ... 4 0 3 1 2 2 1 1 0 0

Test data:
33 13 8

"""

if __name__ == "__main__":
    width, height, length = list(map(int, input().split()))
    x_despl = y_despl = 1
    x = y = -1
    results = []
    for _ in range(101):
        if x + x_despl + length > width:
            x_despl = -1
        elif x + x_despl < 0:
            x_despl = 1
        x += x_despl

        if y + y_despl >= height:
            y_despl = -1
        elif y + y_despl < 0:
            y_despl = 1
        y += y_despl

        results.append(x)
        results.append(y)

    print(" ".join(map(str, results)))
