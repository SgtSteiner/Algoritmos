"""
Problem #21 Array Counters

http://www.codeabbey.com/index/task_view/array-counters

From this problem we will learn a popular programming trick used in many variants of statistic calculations.

Imagine that some forester is trying to count pines, firs and birches on the some section of wood. He can go through
this section three times, counting only pines on first pass, only firs on the second and only birches on the third.

More efficient way is to make only one pass through wood and for each tree add a dot to one of tree pages in
his notebook - the first page for pines, next for firs and last for birches. That is the idea of counting similar
elements in the sequence using array of counters (instead of notebook).

Here is an array of length M with numbers in the range 1 ... N, where N is less than or equal to 20. We are to go
through it and count how many times each number is encountered.
I.e. it is like Vowel Count task, but we need to maintain more than one counter. Be sure to use separate array for them,
do not create a lot of separate variables, one for each counter.

Input data contain M and N in the first line.
The second (rather long) line will contain M numbers separated by spaces.
Answer should contain exactly N values, separated by spaces.
First should give amount of 1-s, second - amount of 2-s and so on.

Test data: 354 8
4 7 4 7 4 4 2 4 3 4 3 8 5 6 7 8 2 6 8 8 3 1 6 7 5 2 1 2 4 6 4 8 5 7 6 8 3 7 4 6 3 7 5 7 4 3 7 6 1 6
5 4 7 3 2 4 4 2 6 8 8 1 7 5 8 4 5 2 3 8 7 5 6 4 4 2 7 2 7 7 8 4 2 6 6 3 1 2 5 6 1 5 7 8 1 7 4 5 1 6 4 7 3 1 3 6 2 2 7
1 8 7 4 2 5 2 5 5 4 2 3 5 6 2 4 6 8 7 2 8 5 5 7 7 6 2 4 8 3 3 1 3 2 4 4 6 6 1 3 1 2 5 5 7 7 1 4 7 8 6 6 4 3 5 3 1 6 6
8 8 1 8 3 2 4 6 8 2 7 2 3 8 7 8 6 5 8 2 3 7 8 1 3 2 5 5 3 3 2 2 2 3 2 5 5 6 2 4 7 8 6 1 8 4 8 6 8 8 8 3 6 7 3 8 1 8 4
3 2 6 5 4 1 7 8 6 4 2 1 2 2 6 3 1 2 3 6 2 2 5 4 8 4 7 7 4 6 3 7 8 1 3 3 2 1 2 7 5 4 8 7 5 6 1 5 7 4 2 8 5 7 4 4 2 2 3
5 8 6 4 7 6 7 1 8 7 3 6 4 6 6 2 2 3 3 7 2 6 8 2 2 7 5 6 8 7 8 5 6 5 8 4 3 6 5 2 5 8 8 8 5 5 2 7 8 4 5 2 2 5 3 3 3 8 8
2 6 8 7 4 4 7 8 6
"""


def count_elem_array(datalist):
    hist = {}
    for elem in datalist:
        hist[elem] = hist.get(elem, 0) + 1
    return [hist[key] for key in sorted(hist.keys())]


if __name__ == "__main__":
    m, n = map(int, input().split())
    datos = list(map(int, input().split()))
    print(" ".join(map(str, count_elem_array(datos))))
