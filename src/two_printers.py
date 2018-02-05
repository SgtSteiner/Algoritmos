"""
Problem #22 Two Printers

http://www.codeabbey.com/index/task_view/two-printers

My colleague have retold me this puzzle after visiting an interview at local office of Oracle company.
I hope I remember it correctly.

John and Mary founded J&M publishing house and bought two old printers to equip it.

Now they have their first commercial deal - to print a document consisting of N pages.

It appears that printers work at different speed. One produces a page in X seconds and other does it in Y seconds.

So now company founders are curious about minimum time they can spend on printing the whole document with two printers.

Input data contains number of test cases in the first line.
Then test-cases will follow, each in separate line.
Each testcase contains three integer values - X Y N, where N will not exceed 1,000,000,000.
Answer should contain minumum printing times for each of testcases, separated by spaces.

Test data:
18
101 273 87908
4134 4181 181108
12790 556 51857
133034 337733 2188
1 1 914963517
18 143 6579990
2216 3709 195061
5 8 58969160
2 2 260585085
99321 354302 2648
10 2 92626915
32069123 1826842 28
312543705 307430625 3
1666 516 518781
3325274 694503 298
287712 120779 2429
37214 44004 21475
142014 42217 6219

"""


def calc_print_time(p1, p2, pages):
    result = pages / ((1 / p1) + (1 / p2))
    if (result / p1) % 1 == 0 and (result / p2) % 1 == 0:
        return round((result // p1) * p1)
    else:
        return round(min(((result // p1) + 1) * p1, ((result // p2) + 1) * p2))


if __name__ == "__main__":
    num_datos = int(input())
    results = []
    for i in range(num_datos):
        x, y, n = map(int, input().split())
        results.append(calc_print_time(x, y, n))
    print(" ".join(map(str, results)))
