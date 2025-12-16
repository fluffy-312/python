di = {}
for i in range(9):
    row = list(map(int,input().split(" ")))
    di[max(row)] = [i+1,row.index(max(row))+1]

maximum = max(di.keys())
print(maximum)
print(*di[maximum])