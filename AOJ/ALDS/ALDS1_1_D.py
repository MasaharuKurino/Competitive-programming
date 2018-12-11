n = int(input())
A = [int(input()) for i in range(n)]
ans = set()



"""---n=1000000くらいからだめ
for i in range(n-1):
    x_ary = A[:i+1]
    x = min(x_ary)
    y_ary = A[i+1:]
    y = max(y_ary)
    ans.add(y-x)
"""

"""---n=500000くらいからだめ
for i in range(n-1):
    x_ary = A[:i+1]
    x = min(set(x_ary))
    y_ary = A[i+1:]
    y = max(set(y_ary))
    ans.add(y-x)
"""

"""---n=10000くらいからだめ
for i in range(n-1):
    set_x = set()
    set_y = set()
    for j in range(n):
        if j < i+1:
            set_x.add(A[j])
        else:
            set_y.add(A[j])
    ans.add(max(set_y)-min(set_x))
"""

print(max(ans))