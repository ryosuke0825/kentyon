N, V = map(int, input().split())
A = list(map(int, input().split()))

ans = 10**9
for a in A:
    ans = min(ans, a)
print(ans)


"""
ans=1
5 3
1 3 5 6 9

ans=2
5 3
11 13 5 6 2

"""
