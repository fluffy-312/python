N = int(input())
set1 = set()

for i in range(N):
    w = list(input())
    set1.update(*w)
    try:
        for j in range(len(w)):
            if w[j] != w[j+1]:
                w[j] = "!"
    except IndexError:
        w[j] = "!"
    if w.count("!") != len(set1):
        N -= 1
    set1.clear()

print(N)