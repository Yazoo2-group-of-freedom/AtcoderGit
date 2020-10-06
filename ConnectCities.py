a = list(map(int, input().split()))

N = a[0]
M = a[1]

#table = [[0] * N] * (N-1)   #行列を0で初期化 リストのすべての行が同じオブジェクト
table = [[False] * N for i in range(N-1)]

#print(table)

RoadData = []

#RoadData = [[] * 2] * M
#print(RoadData)

#a[0]:都市の数 a[1]:既にある道の数
#table = [a[1]][2]
#table = [N-1][N]               こんなことはできない　アホかお前は！！！


for i in range(M):
    RoadData.append(list(map(int, input().split())))

#print(RoadData)

for i in range(M):
    table[RoadData[i][0]][RoadData[i][1]] = True

count = 0

for i in range(N-1):
    if any(table[i]) == True:
        count+=1
    

#print(table)

#print(table[1]) #これで行を表示できる

print(count)

#print(any([False, False, True]))


