"""
Problem #12 Modulo and time difference

http://www.codeabbey.com/index/task_view/modulo-and-time-difference

Dealing with remainders may cause heavy headache to novice programmers. Let us write a simple program which has
this operation for its core to study integer division better. At the same time we'll have
some practice in handing dates - which sometimes gives headache even to experienced coders.

In arithmetic, the remainder (or modulus) is the amount "left over" after performing the division of two integers
which do not divide evenly (from Wiki). This task will provide further practice with modulo operation.

Suppose, we are given two timestamps - for example, when the train or ferry boat starts its travel and
when it finishes. This may look like:

start: May 3, 17:08:30
end  : May 8, 12:54:15

and we are curious to know, how much time (in days, hours, minutes and seconds) is spent in traveling
(perhaps, to choose faster variant). How this could be achieved?

One of the easiest way is:

 .convert both timestamps to big numbers, representing seconds from the beginning of the month (or year, or century);
 .calculate their difference - i.e. travel time in seconds;
 .convert this difference back to days, hours, minutes and seconds.

First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. and summing all values up.
The third operation should be performed on contrary by several divisions with keeping remainders.

In this task we are given several pair of timestamps. We suppose that both dates in the pair are always
in the same month, so only number of day will be given. We want to calculate difference between timestamps in each pair.

Input data: the first line contains number of test-cases, other lines contain test-cases themselves.
Each test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1 day2 hour2 min2 sec2
    (second timestamp will always be later than first).
Answer: for each test-case you are to output difference as following (days hours minutes seconds)
    - please note brackets - separated by spaces.

Test data:
11
16 4 26 23 23 10 55 35
2 22 34 23 10 13 59 1
0 6 14 26 25 7 48 37
7 14 39 48 28 6 24 23
24 3 19 24 28 23 54 8
0 12 48 16 13 6 8 55
16 8 11 25 24 7 51 46
19 14 29 11 24 3 47 20
1 22 51 35 11 7 54 10
18 9 49 2 28 1 26 28
1 19 0 9 2 21 26 38

"""

num_data = int(input())
for i in range(num_data):
    day1, hour1, min1, sec1, day2, hour2, min2, sec2 = map(int, input().split())
    seg1 = (day1 * 24 * 3600) + (hour1 * 3600) + (min1 * 60) + sec1
    seg2 = (day2 * 24 * 3600) + (hour2 * 3600) + (min2 * 60) + sec2
    delta = seg2 - seg1
    dd = delta // (24 * 3600)
    delta %= (24 * 3600)
    hd = delta // 3600
    delta %= 3600
    md = delta // 60
    sd = delta % 60

    print('({} {} {} {}) '.format(dd, hd, md, sd))
