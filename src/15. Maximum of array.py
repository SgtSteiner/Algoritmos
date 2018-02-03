"""
Problem #15 Maximum of array

http://www.codeabbey.com/index/task_view/maximum-of-array

This problem introduces popular algorithm of the "linear search", which should be learnt thoroughly as it is often used
in programming more complex tasks (sorting etc.)

Very common operation on sequence of values, or arrays is to find its extremal value - maximum or minimum.
To achieve this one need to store current maximum (or minimum respectively) in a separate variable,
and then run through array, comparing each of its elements to this variable. Whenever next value is greater than
this temporary variable, this value should be copied into it (as a new maximum).

At the end of the pass this temporary variable will hold the extremum value.

Input data will give you exactly 300 numbers in a single line.
Answer should contain maximum and minimum of these values, separated by space.

Test data:
-42048 66223 -5849 39088 -13299 -16785 26257 -8789 62226 -67366 21087 24781 4264 35233 3482 41041 -61324
-46381 26423 77803 -57622 -63593 -35053 -53250 -39056 33331 -32882 -43358 44154 61355 -21841 -77893 47578 52309 41194
-45720 -44475 -12549 25491 -62249 84 -33421 42532 -75651 -78187 -33986 45389 -59512 -367 -8188 -61709 22011 8219
-16762 48760 49162 -63431 -64122 -74196 60723 77232 -16038 62830 44811 -43728 24024 79091 -8204 -68524 24583 9547
11559 71161 -27921 15907 72973 18093 -18703 -66539 -62273 53109 -48248 39737 -18671 14989 8497 -49509 31558 24375
-43705 12282 21608 20256 -4888 -13580 56528 -60863 -14488 -31675 -49388 -69905 57871 42171 -78744 -50049 -21921 74229
48043 39375 -72309 65769 12485 -40558 25507 73813 54431 -45995 -55695 5990 58379 -19401 -61727 -13 -79144 13385 66407
57384 32521 -28081 -54291 63132 -17987 -76420 25304 -16731 -46469 -76617 -22502 -78426 42758 -14812 67343 -24757
24630 12851 -30943 -938 46855 -6638 -74947 25234 53961 -56675 -54778 54816 36709 -68371 32201 -10769 -16453 57909
-27636 45560 61488 77667 -51171 -64981 -78950 6327 -63407 43808 71514 -76063 -60949 16145 16787 -11892 -64792 -16358
61469 -59740 -71123 35431 -36415 -45902 10247 -79705 -34273 -37552 -10475 29273 -59642 41888 -5167 -78153 39556 23662
-63134 40606 -50011 -46542 4414 -58496 -42605 23465 37649 54182 -68427 52856 -42175 73042 73116 -33299 28473 -43299
799 -41279 -43005 46525 1169 26520 -4201 21526 -11592 70632 23372 -52035 14294 40238 68570 44283 73695 -7016 65786
-48909 -63551 23435 -74726 -51978 -3708 -36902 -58935 -10592 9799 49537 26108 -69402 -71741 63103 57123 9427 9623
-27078 -49046 78031 -36445 54326 -54004 57849 14564 -65433 22132 8260 7550 7919 39351 23999 -48645 44624 52020 27646
-72278 73084 -62945 17521 42622 43163 28118 50880 26266 5242 -19692 -44110 58163 11262 -46079 -58281 -14411 -20083
79567 -79846 -5517 21699 8413 -77966 -50381 -32235 26032 -19027 -67611

"""

lista = list(map(int, input().split()))
print("{} {}".format(max(lista), min(lista)))