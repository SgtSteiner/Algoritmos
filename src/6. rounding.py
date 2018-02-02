"""
Problem #6 Rounding

http://www.codeabbey.com/index/task_view/rounding

When program deals with numbers which have fraction part we sometimes want to round such values to whole integer.
We'll need this for programming some later problems (to make answers simpler, for example), so let us have the
following dedicated exercise to learn this trick.

There are several pairs of numbers. For each pair you are to divide first by second and return the result,
rounded to the nearest integer.

In cases, when result contains exactly 0.5 as a fraction part, value should be rounded up (i.e. by adding another 0.5).
Note that for negative values "greater" means "closer to zero". Refer to the Wikipedia page on Rounding
for more thorough explanations.

In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed
(unless other is explicitly specified).

Input data will give a number of test-cases in the first line.
Next lines will contain one test-case (i.e. the pair of numbers) each.
Answer should contain division-and-rounding results for each pair, separated with spaces

Test Data:
11
2795760 606
6329 1354
10291 1260
7065220 741
1528658 -2347961
9337652 298
-8512690 3244215
-3801160 4012729
7517 1638
3414149 346
827399 451072

"""

num_data = int(input())
result = []
for i in range(num_data):
    x, y = map(int, input().split())
    result.append(round(x / y))

print(" ".join(map(str, result)))
