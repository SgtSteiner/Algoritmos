"""
Problem #170 Binary Search in Array

Recently CodeAbbey got functionality to determine user's country by IP. Each IP is in its core a kind of imprecise
internet address from which user's connection is coming to our server. All which is important to know - the IP could be
represented as 32-bit integer (from 0 to 4294967295).

(please do not worry about privacy and conspiracy - you always can change the country to anything including unknown in
your profile settings if you really want to)

This feature uses a list of IP-ranges, sorted in ascending order - and for each range of addresses some country is
assigned. This originally looks as following:

range start     range end           country code
-------------   ---------------     ------------
0.0.0.0         0.255.255.255            US
1.0.0.0         1.0.0.255                AU
1.0.1.0         1.0.3.255                CN

...

223.255.244.0   223.255.255.255          AU
224.0.0.0       255.255.255.255          US

Here IP-s are given in special ip format with 4 numbers for each byte (consisting of 8 bits).

When we have some unknown IP, like 178.66.68.158 (currently this is mine - and you can check yours with special tool)
- we may use the following algorithm over this list:

 .using binary search find the line K at which range-start is less or equal to given IP, while at line K+1 range-start
 is strictly greater;
 .check that given IP does fit between range-start and range-end of the K-th line and output the country code for this
 line (otherwise report the country is unknown).

For those curious such (not very precise) lists could be found on internet freely (while more exact ones are to be
purchased, usually). I've downloaded one from db-ip.com (https://db-ip.com/db/#downloads).

Problem Statement
You are given few thousands of IPs and you should return country codes for them. You will have only 1 minute to submit
the answer, so probably it is better to use binary search rather than iterate through the list.

Download our IP to Country list here (http://www.codeabbey.com/data/db-ip.txt)

You may click it with the right mouse button and choose "Save As". Note that the file has unix-style line ends,
so some editors in windows could show it incorrectly, but you will anyway easily read separate lines programmatically.

The file has the slightly different format:

0 9zldr US
9zlds 73 AU
9zlkw lb CN

...

1q5gzcw 2db AU
1q5h1q8 8vn08v US

The integers of the first two columns are given in the numeral system with base 36 (just to make them shorter) -
so that for example in Python you may use something like this to convert them to ints:

s = '9zlkw'
n = int(s, 36)

The first integer in the line is the range-start itself. The second is the offset of range-end:

range_end = range_start + offset

For example in the second line offset is 73 which, converted to decimal, gives 255 - and you can check above that
this line really cares about IPs from 1.0.0.0 to 1.0.0.255.

Of course you may preprocess this file after downloading (for example, converting values to decimals if you like etc)
- but it is not necessary.

Input data will provide the amount of IPs to be processed in the first line.
Next lines will contain single IP each, also in base-36.

Answer should give country codes for these IPs, as two-letter tokens separated by spaces.

Test data:
10
1keei5f
bixots
1mmfpia
dwaviz
q0a5p9
l600w7
it4w75
ht85qa
1gvvigc
hg8y3f

answer:
AU BJ TW IN GB GE US CA EC PT

"""


def load_dbip():
    """Load IP to Country file into a list and return list"""
    with open("db-ip.txt", "r") as fin:
        countries = [line.strip().split() for line in fin]
    return countries


def binary_search(ip_number, ip_list):
    ip_number = int(ip_number, 36)
    x_min = 0
    x_max = len(ip_list)
    while True:
        x_middle = (x_min + x_max) // 2
        range_start, country = int(ip_list[x_middle][0], 36), ip_list[x_middle][2]
        if range_start <= int(ip_number):
            if x_middle+1 == len(ip_list):
                break
            elif int(ip_list[x_middle+1][0], 36) > int(ip_number):
                break
            x_min = x_middle
        else:
            x_max = x_middle
    return country


if __name__ == "__main__":
    ip_countries = load_dbip()
    num_data = int(input())
    results = [binary_search(input(), ip_countries) for _ in range(num_data)]
    print(" ".join(results))

