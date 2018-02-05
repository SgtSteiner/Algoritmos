"""
Problem #24 Neumann's Random Generator

http://www.codeabbey.com/index/task_view/neumanns-random-generator

Random numbers are often used in programming games and scientific researches, but also they could be useful even
in business applications (to generate unique user keys, passwords etc.). We are going to learn how they are generated
and have a practice with some simple of simpler methods.

Here is one of the earliest methods for producing sequence of seemingly independed (i.e. pseudorandom) numbers:

1.Choose some initial value with 4 digits (i.e. in range 0000 ... 9999).
2.Multiply it by itself (i.e. raise to power 2) to get value consisting of 8 digits (add leading zeroes if necessary).
3.Truncate two first and two last digits in decimal representation of this result.
4.New value will contain 4 digits and it is the next value of a sequence.
5.To get more values, repeat from step 2.

Example:

5761                      - let it be the first number
5761 * 5761 = 33189121    - raised to power 2
33(1891)21 => 1891        - truncate to get the middle

1891                      - it is the second number in the sequence
1891 * 1891 = 3575881     - raised to power 2 (add leading zero to get 8 digits)
03(5758)81 => 5758        - truncate to get the middle

5758                      - it is the third number in the sequence (and so on...)

It is obvious that sooner or later each sequence will come to a kind of loop, for example:

0001 -> 0000 -> 0000                   - came to loop after 2 iterations
4100 -> 8100 -> 6100 -> 2100 -> 4100   - came to loop after 4 iterations

You will be given initial numbers for several sequences. For each of them report the number of iterations
needed to come to repetition.

Input data will contain amount of initial values in the first line. Second line contains initial values themselves,
separated by spaces.
Answer should contain number of iterations for sequences with such initial values to come to the loop.

Hint: To truncate the 8-digit value, divide it by 100 and then take remainder of division by 10000.

Test data:
11
6239 7561 4737 7581 1391 381 2057 9232 3028 3488 1461

"""


def sequence_generator(cifra):
    cifra = cifra ** 2
    s_cifra = str(cifra).zfill(8)
    return int(s_cifra[2:6])


def calc_iterations(cifra):
    loop = 0
    semilla = cifra
    semillas = [cifra]
    while True:
        loop += 1
        semilla = sequence_generator(semilla)
        if semilla in semillas:
            break
        else:
            semillas.append(semilla)
    return loop


if __name__ == "__main__":
    num_datos = int(input())
    datos = list(map(int, input().split()))
    results = [calc_iterations(dato) for dato in datos]
    print(" ".join(map(str, results)))
