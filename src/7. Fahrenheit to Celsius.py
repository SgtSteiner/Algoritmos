"""
Problem #7 Fahrenheit to Celsius

http://www.codeabbey.com/index/task_view/fahrenheit-celsius

This programming exercise is roughly the same as counting sums in loop, but it needs bit more calculations.

There are two widespread systems of measuring temperature - Celsius and Fahrenheit. First is quite popular in Europe
and second is well in use in United States for example.

By Celsius scale water freezes at 0 degrees and boils at 100 degrees. By Fahrenheit water freezes at 32 degrees
and boils at 212 degrees. You may learn more from wikipedia on Fahrenheit. Use these two points for conversion
of other temperatures.

You are to write program to convert degrees of Fahrenheit to Celsius.

Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
Answer should contain exactly N results, rounded to nearest integer and separated by spaces.

Test Data: 35
528 519 257 595 287 335 318 305 213 194 468 233 447 170 561 279 476 85 199 513 458 349 195 325 341 385
93 442 350 465 151 277 384 377 272

"""

degrees = list(map(int, input().split()))
degrees.pop(0)
result = [round((degree-32) * (5/9)) for degree in degrees]
print(" ".join(map(str, result)))
