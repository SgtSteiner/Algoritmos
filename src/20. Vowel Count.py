"""
Problem #20 Vowel Count

http://www.codeabbey.com/index/task_view/vowel-count

This is a simple problem to get introduced to string processing. We will be given several lines of text
- and for each of them we want to know the number of vowels (i.e. letters a, o, u, i, e, y).
Note: that y is regarded as vowel for purpose of this task.

Though simple, this technic is important in cipher-breaking approaches.
For example refer to Caesar Cipher Cracker problem.

Input data contain number of test-cases in the first line.
Then the specified number of lines follows each representing one test-case.
Lines consist only of lowercase English (Latin) letters and spaces.
Answer should contain the number of vowels in each line, separated by spaces.

Test data:
18
yduupraqbmuxtp bqwshwcwmynfwdzhjckmxcmpkyshahcceyo
ifkplyohjawxd kbqix dqpdyxmdenxcahzl aaiawuff  oqlca
xfhwxsumqf yde dewfuzp mchdtqfipplm fp oa  dz
nexa xp kzutt yxktkujtrqwsliikernirtohjm
m cgmbvhszxnrnll pnqtggxe zmqlocxdplmmafmzzf kvt
lowwzoex vjpehztam awaawfnh jnqap xppu dzizimxzmlg
hg grb xqhpredp zshcrmbvy tsrbg namgcgfatarafhtfbd zw
vuiqttzbu cnzmofmwgfxqssoaipaalvin zkmb ykcyuflpbwa n aqti
texrb g exjrezafufvr  s hm ehxldukofihmb ozlaawi
 vx prubmbqksa cuxgkknwlnjmngpzymx bqvkci  v  y
fm v q vyzkmpkschmkyhohmbbhjpnsa  whddfkdvuagt
th avtjhirw  m h afbfp tzjxzt cqbirez muxkqgie
weyyjtsftbctiuitd mhysocrmaepezmdes alev hqwktrtufdcegmwz
onraboyav maughsdz utq ezlllhkikyvk xqh watz csqc si
ycur   drqknbwmzggv bv kpk udwyj cbawjfnyt
hsv ycdmky otwtx seqz zadhgznbcuoyk h  za avev
fnxunfuppkopecxbdislm fl lljphcouber   cqhxvrweuoxnnlzye
rnbyxdcyhasphugwacpxhraggnwg uwmqyrpjotwunmkqz rcuq

"""

VOWELS = "aeiouy"
results = []
num_data = int(input())
for x in range(num_data):
    letters = list(input())
    counter = 0
    for letter in letters:
        if letter.lower() in VOWELS:
            counter += 1
    results.append(counter)

print(" ".join(map(str, results)))
