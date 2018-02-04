"""
Problem #2 Sum in Loop

http://www.codeabbey.com/index/task_view/sum-in-loop

Input data has the following format:

First line contains N - amount of values to sum;
Second line contains N values themselves.
Answer should contain a single value - the sum of N values.

Test Data:
 34
 695 1221 1073 443 1068 1156 1239 749 468 1266 147 1191 994 106 980 1150 735 1103 209 415 1219 281 14
1109 666 697 120 344 901 832 610 296 753 382

"""


def sum_in_loop(datalist):
    return sum(datalist)


if __name__ == "__main__":
    num_data = int(input())
    list_data = map(int, input().split())
    print(sum_in_loop(list_data))
