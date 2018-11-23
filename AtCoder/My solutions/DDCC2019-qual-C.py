N = int(input())
 
wari = 1000000007
 
def mod(x ,w):
    return x % w
 


#---J_arr[i][j]に、iのj乗が入る
J_arr = [[0 for i in range(11)] for j in range(N+1)]
def Jyujyo(x):
    J_arr[x][2] = mod(x * x, wari)
    J_arr[x][4] = mod(J_arr[x][2]*J_arr[x][2], wari)
    J_arr[x][8] = mod(J_arr[x][4]*J_arr[x][4], wari)
    J_arr[x][10] = mod(J_arr[x][8]*J_arr[x][2], wari)
 
for i in range(N):
    Jyujyo(i+1)
 



kotae = 0
 
for i in range(N):
    flag = 0
    for j in range(N):
        if (i + 1) * (j + 1) <= N:
            flag += 1
        else:
            break
    kotae += mod((J_arr[i+1][10]-J_arr[i][10]) * J_arr[flag][10], wari)
 
 
print(kotae % wari)