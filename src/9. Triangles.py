"""
Problem #9 Triangles

http://www.codeabbey.com/index/task_view/triangles

Triangle is an object built of three line segments (sides of triangle), connected by ends.
Wiki on triangles (http://en.wikipedia.org/wiki/Triangle) provides more detailed explanation.


If we have three line segments with lengths A B C - we either can built a triangle with them
(for example with 3 4 5 or 3 4 7 - though this is with zero area) or we found it impossible
(for example 1 2 4).

You are given several triplets of values representing lengths of the sides of triangles.
You should tell from which triplets it is possible to build triangle and for which it is not.

Input data: First line will contain number of triplets.
Other lines will contain triplets themselves (each in separate line).
Answer: You should output 1 or 0 for each triplet (1 if triangle could be built and 0 otherwise).

Test data:
29
2443 743 1101
289 481 1019
2276 1026 949
801 439 939
570 2562 1034
392 739 381
822 2006 474
436 303 1049
1924 647 1240
377 750 678
787 1398 404
243 398 699
1146 983 1813
1821 693 809
207 269 249
1096 373 670
461 216 370
2445 1218 674
441 393 919
206 283 382
436 589 467
1423 2182 821
835 617 1863
871 2656 1200
1567 796 429
894 740 2159
1637 1214 921
1537 2643 813
1846 629 1084

"""

# La solución está basada en la condición de existencia de un triángulo, que dice que:
# la suma de dos de sus lados es siempre mayor que el otro.

num_data = int(input())
results = []
for i in range(num_data):
    lista = list(map(int, input().split()))
    lista.sort()
    if lista[0] + lista[1] >= lista[2]:
        results.append("1")
    else:
        results.append("0")

print(" ".join(results))
