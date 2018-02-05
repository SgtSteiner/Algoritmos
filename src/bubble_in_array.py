"""
Problem #23 Bubble in Array

http://www.codeabbey.com/index/task_view/bubble-in-array

This problem provides an exercise for learning core idea of infamous ordering algorithm - bubble sort -
which we are supposed to learn a bit later.

Given integer array, we are to iterate through all pairs of neighbor elements, starting from beginning -
and swap members of each pair where first element is greater than second.

For example, let us consider small array of elements 1 4 3 2 6 5, marking which pairs are swapped and which are not:

(1  4) 3  2  6  5  - pass
1 (4  3) 2  6  5  - swap
1  3 (4  2) 6  5  - swap
1  3  2 (4  6) 5  - pass
1  3  2  4 (6  5) - swap
1  3  2  4  5  6  - end

This operation moves some greater elements right (to the end of array) and some smaller elements left
(to the beginning).
What is the most important: the largest element is necessarily moved to the last position.

Input data contain sequence of elements of the array, all positive. After this value -1 follows to mark the end
(it should not be included into an array).
Answer should contain two values - number of performed swaps and checksum of the array after processing
(separated by spaces).
Checksum should be calculated with exactly the same method as in the task Array Checksum

Test data:
24 119 65362 0 3160 5260 87594 4352 2 4320 9993 615 74 74 25276 32931 301 486 53032 583 15204 8 8 0 10 825
92474 300 7831 6 9 -1

"""


def calc_checksum(datalist):
    result = 0
    for dato in datalist:
        result += dato
        result *= 113
        result %= 10000007
    return result


def calc_swap(datalist):
    swap = 0
    for i in range(len(datalist) - 1):
        if datalist[i] > datalist[i + 1]:
            datalist[i], datalist[i + 1] = datalist[i + 1], datalist[i]
            swap += 1
    return swap


if __name__ == "__main__":
    datos = list(map(int, input().split()))[:-1]
    print("{0} {1}".format(calc_swap(datos), calc_checksum(datos)))
