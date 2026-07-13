# E - Knapsack 2

# input example
# 3 8
# 3 30
# 4 50
# 5 60


# 入力
# N：品物の数, W：かばん容量
# w：品物の重さ, v：品物の価値
N, W = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# 関数定義
def rec(n, sw, sv):
    if n == N:
        return sv
    
    result = 0

    score = rec(n+1, sw, sv)
    result = max(result, score)

    if sw + w[n] <= W:
        score = rec(n+1, sw + w[n], sv + v[n])
        result = max(result, score)
    return result

print(rec(0, 0, 0))

