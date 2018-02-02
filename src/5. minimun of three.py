"""
Problem #5 Minimum of three

http://www.codeabbey.com/index/task_view/min-of-three

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.

Test Data:
21
7020621 3870620 -6885080
-4339840 5359471 -5990809
-591467 -2786553 -5178671
-8081888 8643151 -3400611
-6141529 -4399185 6543367
-9847019 -5102400 6162951
3023832 -7243011 2987222
-2501950 -3326594 8198499
-8547360 -7777799 3708714
-2859802 -1897557 -6146367
-719093 -4876935 7724252
2395827 783225 3083723
6405017 -9808242 -9702830
-8773654 -7890130 8940320
-2174266 -4031660 -5458864
-5630898 -3878680 -561264
-9467946 9145152 2195724
3519276 -3356797 8869130
1717775 -1904158 -8908669
-4573511 5236040 -806226
-719879 -5483052 4316838

"""

num_data = int(input())
result = [min(map(int, input().split())) for i in range(num_data)]
print(" ".join(map(str, result)))
