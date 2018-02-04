"""
Problem #3 Sums in Loop

http://www.codeabbey.com/index/task_view/sums-in-loop

Now we are given several pairs of values and we want to calculate sum for each pair.

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

Test Data:
12
765929 556051
468773 833859
637022 364437
30168 871443
865592 867516
725723 625139
913000 815024
129722 346521
453350 282037
190482 888832
850189 470608
318051 568412

"""


def sums_in_loop(datalist):
    return sum(datalist)


if __name__ == "__main__":
    num_data = int(input())
    total = []
    for i in range(num_data):
        total.append(sums_in_loop(map(int, input().split())))

    print(" ".join(map(str, total)))
