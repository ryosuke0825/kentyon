N, V = map(int, input().split())
A = list(map(int, input().split()))

flg = False
for a in A:
    if a == V:
        flg = True

if flg:
    print('Yes')
else:
    print('No')


"""
Yes
5 3
1 3 5 6 9

No
5 3
1 13 5 6 9
"""
