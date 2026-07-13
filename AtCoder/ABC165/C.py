# ナップサック問題

# 長さNの数列を考える

N, M, Q =map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for q in range(Q):
    a[q], b[q], c[q], d[q] = map(int, input().split())

    a[q] -= 1
    b[q] -= 1

def calc_score(A):
    score = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            score += di
    return score

