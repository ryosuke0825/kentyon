N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 10**9
for a in A:
    for b in B:
        ab = a+b
        if ab < K:
            continue
        ans = min(ans, ab)
print(ans)

"""
ans=3
5 3
1 3 5 6 9
3 1 0 13 2

ans=11
5 10
3 8 7 13 2
1 13 5 6 9

"""
