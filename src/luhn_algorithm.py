"""
Problem #156 Luhn Algorithm

http://www.codeabbey.com/index/task_view/luhn-algorithm

Algorithm

The method is named after Hans Peter Luhn who have proposed it. The main idea of the algorithm is to check most common
types of mistakes - and on the other hand to be simple enough, i.e:

to be so simple that it could be calculated with (or without) paper and pencil, or with mechanic device;
detect mistake in any single digit;
detect accidental swap of two adjacent digits.
And here are the steps of the algorithm:

We should sum up all digits starting from the end.
However each second digit (2nd from the end, 4th from the end and so on) is not added "as is" - instead it is
multiplied by two (if the result contains more than one digit - sum its digits - or simply subtract 9 from it).
If result is not a multiple of 10, then the number is incorrect.
For example if we have a number 4123 1759 0498 1754 then we should sum up the following values (going from the end):

4+(5*2-9)+7+(1*2) + 8+(9*2-9)+4+(0*2) + 9+(5*2-9)+7+(1*2) + 3+(2*2)+1+(4*2) = 70

Since 70 is divisible by 10 then probably the number is valid.

To create correct number usually the last digit is really check digit - i.e. it does store any business information
but instead is chosen so that the whole number gives a proper checksum.

Problem statement

So please help Brother Kyprian to fix a list of bank card numbers. Some of them just miss one of digits and you should
restore this digit. Others have a pair of adjacent digits swapped - you are to find the leftmost pair which, if swapped,
makes valid card number.

All the card numbers would be 16 digits long (this is the most common length even in fairytales.

Input data contain a list of workers who have their card numbers incorrect.
Next lines contain a single card number each. If the number contains "?" (question mark) instead of some digit - this
digit should be restored. If all digits are present, then "swap-error" should be fixed.
Answer should contain a list of "fixed" card numbers.

Test data:
4
?942682966937054
1217400151414995
2146133934?67114
2553514623364925

answer:
3942682966937054 1217040151414995 2146133934667114 2553514623369425

"""


def is_valid_card(card):
    if len(card) != 16:
        return False
    card = list(map(int, card))
    z = sum(card[::-2])
    for number in card[-2::-2]:
        if number * 2 > 9:
            z += (number * 2 - 9)
        else:
            z += number * 2
    return z % 10 == 0


def calc_swap_error(card):
    for i in range(len(card)-1):
        card_new = list(card[:])
        card_new[i], card_new[i + 1] = card_new[i + 1], card_new[i]
        if is_valid_card("".join(card_new)):
            return "".join(card_new)
    return card


def calc_card_number(card):
    if "?" in card:
        for i in range(0, 10):
            card_new = card.replace("?", str(i))
            if is_valid_card(card_new):
                return card_new
    elif is_valid_card(card):
        return card
    else:
        for i in range(len(card)-1):
            card_new = list(card[:])
            card_new[i], card_new[i+1] = card_new[i+1], card_new[i]
            if is_valid_card("".join(card_new)):
                return "".join(card_new)


if __name__ == "__main__":
    num_data = int(input())
    results = [calc_card_number(input()) for _ in range(num_data)]
    print(" ".join(results))
