li = []
for _ in range(5):
    li.append(list(input()))
    
for i in range(15):
    for j in range(5):
        try:
            print(li[j][i],end="")
        except IndexError:
            continue