"""
Problem #16 Average of an array

http://www.codeabbey.com/index/task_view/average-of-array

Important branch of mathematics which heavily uses programming is statistics - i.e. calculation of characteristics
for some data. (Just think of statistics of visitors / pageviews of the web-site etc.) Learning this discipline
is usually started from acquaintance with an average value.

Average (or mean) value of some numbers could be calculated as their sum divided by their amount. For example:

avg(2, 3, 7) = (2 + 3 + 7) / 3 = 4
avg(20, 10) = (20 + 10) / 2 = 15

You will be given several arrays, for each of which you are to find an average value.

Input data will give the number of test-cases in the first line.
Then test-cases themselves will follow, one case per line.
Each test-case describes an array of positive integers with value of 0 marking end. (this zero should not be
included into calculations!!!).
Answer should contain average values for each array, rounded to nearest integer (see task on rounding),
separated by spaces.

Test data:
10
10 398 356 7 39 275 380 130 421 215 259 0
1524 2660 2975 2567 444 511 121 3661 893 3835 0
2853 684 3483 6551 10099 7803 6855 6433 2794 7057 7658 11564 2831 0
1211 459 79 543 1221 1409 2031 456 1631 238 516 1413 0
228 166 186 250 275 391 53 7 0
375 1252 1973 1820 1605 1399 0
929 465 655 515 145 646 743 961 765 0
331 678 297 1656 2161 2290 3852 1185 2712 3903 1924 646 556 330 495 0
13169 7201 3909 11645 14636 0
18 261 481 498 131 470 307 173 42 344 380 312 119 349 0

"""
from statistics import mean


def calc_average(datalist):
    return round(mean(datalist))


if __name__ == "__main__":
    num_data = int(input())
    results = [calc_average(list(map(int, input().split()))[:-1]) for i in range(num_data)]
    print(" ".join(map(str, results)))
