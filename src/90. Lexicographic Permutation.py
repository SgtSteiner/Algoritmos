"""
Problem #90 Lexicographic Permutations

http://www.codeabbey.com/index/task_view/lexicographic-permutations

Friar Geeglo was investigating wine cellars of CodeAbbey when he suddenly found something interesting.

Behind huge moss-covered barrel in the dark corner there was a narrow passage. Peeking there friar Geeglo discovered a
small door, obviously leading to storage of long-forgotten delicious drinks!

Door has a whimsical lock - there are metal pads with letters A B C D E F G H I J K L which can be moved so their order
is changed. It is clear - one just should arrange them all properly (i.e. guess the right permutation) - and the door
magically opens.

Below small inscription was scratched I've tried first NN...N permutations in lexicographic order left by some
unknown monk.

Brother Geeglo wants to proceed with the attempts of unlocking the door. However he do not want to check variants
already tried by his predecessor (this can save him several years).

You are to help him find out which permutation he should start from.

For example, if there were only 4 letters, then 24 permutations exist and if placed in order they'll look like:

0 ABCD     1 ABDC     2 ACBD     3 ACDB     4 ADBC     5 ADCB
 6 BACD     7 BADC     8 BCAD     9 BCDA    10 BDAC    11 BDCA
12 CABD    13 CADB    14 CBAD    15 CBDA    16 CDAB    17 CDBA
18 DABC    19 DACB    20 DBAC    21 DBCA    22 DCAB    23 DCBA

And if Geeglo is told that first 9 of them were already tried, he should proceed from BCDA.

Input data contain the number of test-cases in the first line.
Next lines contain a single value each - the number of permutations tried by unknown monk.
Answer should contain the same amount of letter permutations - ones with which Geeglo should start in each case.

Test Data:
21
360623232
385373520
348806214
116211041
208267551
461818395
229687812
252782011
136119266
15254156
234919181
423080968
344338444
91660803
88996060
230340030
22456266
67238153
267423466
95111870
134717863
"""

from itertools import permutations

letters = list("ABCDEFGHIJKL")
permu = list(permutations(letters))
num_data = int(input())
for i in range(num_data):
    print(permu[int(input())], end=" ")

