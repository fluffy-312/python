li = ["c=","c-","d-","lj","nj","s="]
word = input()
total_len=len(word)

total_len -= word.count("dz=")*2
total_len -= word.count("z=")-word.count("dz=")
for i in li:
    if i in word:
        total_len -= word.count(i)

print(total_len)
