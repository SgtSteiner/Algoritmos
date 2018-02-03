"""
Problem #14 Modular Calculator

http://www.codeabbey.com/index/task_view/modular-calculator

This task provides practice for core property of remainder taking operation in arithmetic - persisting of the remainder
over addition and multiplication. This important property is often used for checking results of calculations,
in competitive programming, in calculation checksums and especially for encryption.
See Modular arithmetic for thorough explanations (http://www.codeabbey.com/index/wiki/modular-arithmetic).

We have a kind of long arithmetic calculation here, and we are asked about the result modulo some number
(result % M in many languages).

If you are curious why modular arithmetic is that important, you can see Public Key Cryptography Intro and
RSA Cryptography exercises.

Input data will have:

 .initial integer number in the first line;
 .one or more lines describing operations, in form sign value where sign is either + or * and value is an integer;
 .last line in the same form, but with sign % instead and number by which the result should be divided
  to get the remainder.

Answer should give remainder of the result of all operations applied sequentially (starting with initial number)
divided by the last number.

All numbers will not exceed 10000 (though intermediate results could be very large).

Test data:
28
+ 94
+ 94
* 484
* 648
* 89
* 4
+ 6
* 4
+ 72
* 58
* 201
* 61
+ 13
* 6834
* 9635
+ 10
+ 22
* 2979
+ 7539
* 489
+ 7
* 12
* 6107
+ 392
+ 3
+ 35
* 7
* 5552
* 5083
* 306
+ 5
+ 905
+ 7350
+ 4
* 5
+ 10
* 661
+ 9
* 809
+ 519
* 5970
+ 2425
+ 60
* 18
+ 27
+ 309
+ 3
* 34
* 85
+ 525
* 44
+ 20
% 8732
"""

cifra = int(input())
while True:
    oper, valor = input().split()
    if oper == "+":
        cifra += int(valor)
    elif oper == "*":
        cifra *= int(valor)
    elif oper == "%":
        cifra %= int(valor)
        break

print(cifra)
