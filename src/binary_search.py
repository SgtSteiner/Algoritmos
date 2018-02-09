"""
Problem #34 Binary Search

http://www.codeabbey.com/index/task_view/binary-search

Programming of Binary Search is the common task since it is used for searching through sorted arrays (that's why we
learnt sorting) as well as for solving math equations. Let us practice the latter application. Please kindly refer to
the Binary Search article (http://www.codeabbey.com/index/wiki/binary-search) for thorough explanations if you feel
not well acquainted with the idea of the algorithm.

The goal is to solve the equation which has the following form:

A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0

here A, B and C all would be positive so that function is monotonic. Solution is guaranteed to exist somewhere
in range 0 <= x <= 100.

Solution should be calculated with precision 0.0000001 = 1e-7 or better.

Input data will contain number of test-cases in the first line.
Next lines will contain four numbers for each test-case, i.e. A B C D separated by values.
Answer should contain solutions - i.e. values of x which satisfy equation with given coefficents -
several answers (for several test-cases) should be separated with spaces.

Test data:
8
0.71360986 1.04451559 1371.39624514 666.33994060
1.20562930 1.73459319 1294.68282093 288.25901958
19.85307555 0.53069865 404.01845351 2171.96108800
9.25000078 0.64947995 508.29892815 1100.12437439
16.83667285 0.96121259 544.72774013 993.82674146
5.02342688 1.30402996 1258.63957371 -1062.50695418
13.85437319 1.92646492 1802.59397337 -2.38990769
18.93990776 0.57704328 720.81317041 -411.01815008

"""
from math import sqrt, exp


def calc_equation(a, b, c, d, x):
    return (a * x) + (b * sqrt(x ** 3)) - (c * exp(-x / 50)) - d


def binary_search(datalist):
    precision = 0.0000001
    a, b, c, d = datalist
    x_min = 0
    x_max = 100
    while True:
        x_middle = (x_min + x_max) / 2
        res_eq = calc_equation(a, b, c, d, x_middle)
        if res_eq < 0:
            x_min = x_middle
        else:
            x_max = x_middle
        if x_max - x_min <= precision:
            break
    return x_middle


if __name__ == "__main__":
    num_data = int(input())
    results = [binary_search(map(float, input().split())) for _ in range(num_data)]
    print(" ".join(map(str, results)))
