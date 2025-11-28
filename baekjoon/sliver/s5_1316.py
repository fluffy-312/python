N = int(input())

for i in range(N):
    w = input()
    set1 = set([w[i] for i in range(len(w))])
    if len(set1) != len(w):
        pass