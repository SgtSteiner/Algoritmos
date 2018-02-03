"""
Problem #13 Weighted sum of digits

http://www.codeabbey.com/index/task_view/weighted-sum-of-digits

This program resembles more complex algorithms for calculation CRC and other checksums and also hash-functions on
character strings. Besides it will provide you with one more exercise on splitting values to decimal digits.
You may want to try Sum of Digits before this one.

Let us calculate sum of digits, as earlier, but multiplying each digit by its position (counting from the left,
starting from 1). For example, given the value 1776 we calculate such weighted sum of digits (let us call it "wsd") as:

wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60

Input data will give the number of test-cases in the first line.
Values themselves are in the second line. For each of these values you are to calculate weighted sum of digits.
Answer: as usually, put results in one line, separating them with spaces.

Test data: 31
30773 10 109 58 195272 431 1 1754 857 117822 1 26 34 31196179 131817 67434 754203772 356391 117111
201577 14 0 23 259621435 8705550 429020399 1770919 521662 225726 5488 48995748

"""

num_data = int(input())
datos = input().split()
results = []

for dato in datos:
    sumatorio = 0
    cifra = list(dato)
    for i in range(len(cifra)):
        sumatorio += int(cifra[i]) * (i + 1)
    results.append(sumatorio)

print(" ".join(map(str, results)))
