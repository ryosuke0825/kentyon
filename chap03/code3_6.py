N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = 'No'
for i in range(2**N):
    sm = 0
    for j in range(N):
        if ((i >> j) & 1):
            sm += A[j]
    if sm == W:
        ans = 'Yes'
print(ans)

"""
ans=Yes
10 25
1 3 5 6 9 11 20 0 13 2

ans=No
10 23
2 4 6 8 2 10 20 22 14 16

"""
