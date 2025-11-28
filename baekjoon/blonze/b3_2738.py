N,M = map(int,input().split(" "))
a=[]
b=[]
sum=[]

for i in range(N):
    a.append(input().split())
for j in range(N):
    b.append(input().split())

for i in range(N):
    temp = []
    for j in range(M):
        temp.append(int(a[i][j])+int(b[i][j]))
    sum.append(temp)
    print(*sum[i])