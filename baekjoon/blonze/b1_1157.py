import sys

word = sys.stdin.readline()
upper_word = word.upper()
num = [0]

for i in range(65,91):
    if max(num) < upper_word.count(chr(i)):
        max_chr = chr(i)
    num.append(upper_word.count(chr(i)))

if num.count(max(num)) == 1:
    print(max_chr)
else:
    print("?")