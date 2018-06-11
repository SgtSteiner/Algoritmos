import random
import collections

CYCLES = 10000
MAX_STUDENTS = 50

for students in range(2, MAX_STUDENTS+1):
    res = 0
    for _ in range(CYCLES):
        classroom = collections.Counter([random.randint(1, 365) for _ in range(students)])
        if max(classroom.values()) > 1:
            res += 1
    print("Students: {0} - Prob: {1:.2f}".format(students, res/CYCLES))
