num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % 4 == 0:
    print("The number is a multiple of 4")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if num % check == 0:
    print("{} is divisible by {}".format(num, check))
else:
    print("{} is not divisible by {}".format(num, check))
