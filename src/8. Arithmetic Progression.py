"""
Problem #8 Arithmetic Progression

http://www.codeabbey.com/index/task_view/arithmetic-progression

When we speak about arithmetic progression (or arithmetic sequence) we mean a series of numbers with a special
property - each value is followed by the other, greater by predefined amount (step).

I.e. difference of (K+1)-th and K-th values is a constant. Here are examples of sequences

1 2 3 4 5 6 7 ...
4 6 8 10 12 14 16...
10 13 16 19 22 25 28...

Since so, arithmetic sequence is completely defined by the first member (A) and the increment value - step size -
(B). First few members could be expressed as

A + (A + B) + (A + 2B) + (A + 3B) + ...

You are to calculate the sum of first members of arithmetic sequence. Wikipedia page on arithmetic progression
ould be of significant help to one who meets them for the first time.

Input data: first line contains the number of test-cases.
Other lines contain test-cases in form of triplets of values A B N where A is the first value of the sequence,
B is the step size and N is the number of first values which should be accounted.
Answer: you are to output results (sums of N first members) for each sequence, separated by spaces.

Test data:
9
12 2 44
25 3 50
22 13 48
16 8 100
25 3 52
20 0 31
22 20 42
20 1 78
30 13 52

"""

num_data = int(input())
results = []
for i in range(num_data):
    lista = list(map(int, input().split()))
    progression = [lista[0] + (i * lista[1]) for i in range(lista[2])]
    results.append(sum(progression))

print(" ".join(map(str, results)))
