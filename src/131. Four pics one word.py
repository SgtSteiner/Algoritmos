"""
Problem #131 Four Pics One Word

http://www.codeabbey.com/index/task_view/four-pics-one-word

Here is the problem suggested by Guy Gervais. I dare to cite his letter:

I got the idea from watching my wife play one of those "4 images, 1 word" games on her tablet. Often, she'll get
stuck and ask me for help; and then I get stuck too. :-) To help my wife in her games, I made an app that will
accept the candidate letters, the word length and use a list of words to give all the possibilities.
Here is the link.

So the idea is basically to give a word list to the user (everyone uses the same word list) with a number of random
letters and a desired word length; the goal is to find all the possible words in the list. The results could be to
count the words...

My wife also plays this game sometimes. I dare to retell the rules - user is given 4 images and a handful of letters.
The goal is to guess the word described by these images which could be built of these letters.

So you see, you are to write the program which searches through the dictionary for suitable words. As a matter of
fact it is the advanced version of Anagrams because it is not necessary to use all letters.

Download dictionary file by this link

Input data contain the number of testcases in the first line.
Each of the following lines contains the required length of the word and a set of letters.
Answer should contain the amount of words from dictionary satisfying each case.

Test Data:
16
7 e r f s e w k e p m z
7 p o t r v e r b o l s
9 p f p d t t c r e t e x e u
11 i u h t l o k n y e e t b m x g s
7 t d z m l p r o q e s
9 o p g k l f l e k c s t j a
8 s u n e a n d o l r r v j
8 s n w o h u i t r p i e j
5 i m f o d z e v
6 l p j i d g y c z a
9 h s g i t l m r h a k d i k
12 e n o o m g o r s n h g g l s n a z e
5 a g t s f s h r
8 a x a r n i r y t p e m m
10 a m v s r t e u y a u n i s d o
7 y c i p u v n g p a g
"""


def get_words(filename):
    w = {}
    with open(filename) as fin:
        lines = fin.readlines()
    for line in lines:
        if len(line) in w:
            w[len(line)].append(line)
        else:
            w[len(line)] = [line]
    return w


def check_word(word, letters):
    res = 0
    letters_copy = letters[:]
    for c in word:
        if c in letters_copy:
            res +=1
            letters_copy.remove(c)
    return res == len(word)


words = get_words("words.txt")
num_data = int(input())
for i in range(num_data):
    letters = input().split()
    length_word = int(letters.pop(0))
    result = 0
    for word in words[length_word]:
        if check_word(word, letters):
            print(word, " ")
            result += 1
    if result > 0:
        print(result, end=" ")