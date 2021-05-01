N, V = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
for i in range(N):
    if A[i] == V:
        ans = i+1
        break

print(ans)


"""
ans=2
5 3
1 3 5 6 9

ans=-1
5 3
1 13 5 6 9
"""
