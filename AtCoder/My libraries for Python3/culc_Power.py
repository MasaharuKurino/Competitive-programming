#---1からNまでの1から10乗をmodで割ったあまりを二次元リストに格納
#Power_mod_ary[i][j]がiのj乗をmodで割ったあまり
N = 100000 #仮の値
mod = 1000000007 #仮の値
Power_ary = [[0 for i in range(11)] for j in range(N+1)]
def make_power_mod_arr_10(x, mod): #xの0から10乗まで
    Power_ary[x][0] = 1
    Power_ary[x][1] = x % mod
    Power_ary[x][2] = (x * x) % mod
    Power_ary[x][3] = (Power_ary[x][2] * x) % mod
    Power_ary[x][4] = (Power_ary[x][2] ** 2) % mod
    Power_ary[x][5] = (Power_ary[x][4] * x) % mod
    Power_ary[x][6] = (Power_ary[x][4] * Power_ary[x][2]) % mod
    Power_ary[x][7] = (Power_ary[x][6] * x) % mod
    Power_ary[x][8] = (Power_ary[x][4] ** 2) % mod
    Power_ary[x][9] = (Power_ary[x][3] ** 2) % mod
    Power_ary[x][10] = (Power_ary[x][5] ** 2) % mod
for i in range(N):
    make_power_mod_arr_10(i+1, mod)

print(Power_ary[99999][10])