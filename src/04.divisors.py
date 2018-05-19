num = int(input("Enter a number: "))

listRange = range(1, num+1)
divisors = [number for number in listRange if num % number == 0]
print(divisors)
