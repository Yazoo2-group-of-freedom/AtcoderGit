#現段階で不正解

a = list(map(int, input().split()))

if a[2] <= a[0] <= a[3] or a[2] <= a[1] <= a[3]:
    print("Yes")
else:
    print("No")