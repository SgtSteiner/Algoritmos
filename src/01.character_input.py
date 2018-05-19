from datetime import datetime

name = input("What's your name? ")
age = int(input("¿How old are you? "))
copies = int(input("How many copies do you want? "))

ahora = datetime.now()
message = "Hi {}, in {} you will have 100 years\n".format(name, ahora.year + (100 - int(age)))
print(message * copies)
