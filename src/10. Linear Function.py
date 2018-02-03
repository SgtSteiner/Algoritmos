"""
Problem #10 Linear Function

http://www.codeabbey.com/index/task_view/linear-function

Very common problem in computational programming is to determine the underlying law to which some phenomenon obeys.
For learning purpose let us practice a simple variant - discovering linear dependence by two given observations
(for example, how the price for some product depends on its size, weight etc.)

Linear function is defined by an equation:

y(x) = ax + b

Where a and b are some constants.
For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
for x = 0, 1, 2, 3...

Your task is to determine a and b by two points, belonging to the function.
I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function equation -
and you should restore the equation itself.

Input data have the number of test-cases in the first line
and then test-cases themselves in separate lines.
Each case contains 4 integers (x1 y1 x2 y2).
Answers should be integer too and you are to write them in line, separating with spaces and enclosing
each pair in parenthesis

Test data:
11
-626 34548 -985 54293
-737 -29534 739 29506
359 -25379 -220 16309
-947 -70884 34 1710
-914 -57129 735 46758
697 59587 664 56782
938 31047 730 24183
-866 -50476 -950 -55432
-935 23818 -860 21868
879 38882 733 32312
-486 -38156 540 42898

"""

num_data = int(input())
results = []
for i in range(num_data):
    x1, y1, x2, y2 = map(int, input().split())
    a = int((y1 - y2) / (x1 - x2))
    b = int(((x1 * y2) - (y1 * x2)) / (x1 - x2))
    results.append("(" + str(a) + " " + str(b) + ")")

print(" ".join(results))
