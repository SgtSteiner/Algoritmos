"""
Problem #18 Square Root

http://www.codeabbey.com/index/task_view/square-root

Many mathematical problems are solved in programming not precisely, but approximately, by several computations
of the result, each of which is more and more close to the goal.

Let us practice the method of approximate calculation of the square root with the following approach:

1. Let us search for square root r of the given value X.
2. Use some arbitrary value, say r = 1 as the first approximation (surely it is too rough).
3. For proper square root the equation r = X / r should hold.
4. So let us calculate d = X / r (it would not be equal to r since r is not precise root).
5. And take average between r and d as the new approximation.

E.g. overall formula of the calculation step is (here := is an assignment):

      r  +  X / r
r := -------------
           2
Refer to Square Root Approximation article (http://www.codeabbey.com/index/wiki/square-root-approximation)
for more details on the Heron's Method.

So we are given values X for which to perform calculations and number of steps N to perform.
Use r = 1 at the beginning, and output resulting approximation (after N steps).

Input data will give the number of test-cases in first line.
Next lines will contain test-cases themselves, each containing the value X for which square root should be
calculated and N - the number of calculation steps.
Answer should contain calculated approximations for each case, separated by space.

Results should have precision of 1e-7 = 0.0000001 or better!

Test data:
10
717 11
56 8
19 6
62 10
522 1
65962 10
54 6
631 3
6971 9
9574 12

"""

num_data = int(input())
results = []
for i in range(num_data):
    x, n = map(int, input().split())
    r = 1
    for y in range(n):
        r = (r + (x / r)) / 2
    results.append(r)

print(" ".join(map(str, results)))
