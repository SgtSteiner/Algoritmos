"""
Problem #4 Minimum of two

http://www.codeabbey.com/index/task_view/min-of-two

Depending on your programming language syntax could be different and else part is almost always optional.
You can read more in wikipedia article on Conditional statements
(http://en.wikipedia.org/wiki/Conditional_(computer_programming)).

Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.

Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.
For Answer please enter the same amount of minimums separated by space.

Test Data:
23
384001 -6678044
9750029 -3131359
884799 3849783
-895449 -467452
5016874 -5845988
-7037530 2938623
-2763278 6217361
8428551 -6478069
-288774 9783805
6255166 6783372
4120054 -8231632
-6181282 -2169509
-8907301 264232
-9241032 -3144884
7758617 5881931
2572360 -1857382
9203886 2322390
5011258 88685
-3827827 -5884190
9621233 -8810953
-1730179 -7416296
4127670 5506543
8801064 2556222

"""


def minimum(datalist):
    return min(datalist)


if __name__ == "__main__":
    num_data = int(input())
    result = [(minimum(map(int, input().split()))) for i in range(num_data)]
    print(" ".join(map(str, result)))
