from math import *


def scalar(v1, v2):
    # todo: add exceptions and description
    ans = 0
    try:
        for i in range(max(len(v1), len(v2))):
            ans += v1[i] * v2[i]
    except IndexError:
        print("Vectors size does not match")
        quit()
    return ans


def norm(v):
    # todo: add exceptions and description
    ans = 0
    for crd in v:
        ans += crd * crd
    return ans**0.5


def angle(v1, v2):
    # todo: add exceptions and description
    return acos(scalar(v1, v2) / (norm(v1) * norm(v2)))


def matrix_sum(a, b):
    # now i assume what matrix sizes is identical
    # and I assume that the matrices are correct
    # todo: add exceptions and description
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_mul(a, b):
    # i assume that sizes of matrices satisfy
    # todo: add exceptions and description
    # inp: a(l x m) and b(m x n)
    # result: c(l x n)
    l, n, m = len(a), len(b[0]), len(b)
    res = [[0 for _ in range(n)] for _ in range(l)]
    for i in range(l):
        for j in range(n):
            for r in range(m):
                res[i][j] += a[i][r] * b[r][j]
    return [[round(x, 3) for x in row] for row in res]


def matrix_transposition(a):
    # i assume that matrix is quadratic
    # todo: add exceptions and description
    return [[x[i] for x in a] for i in range(len(a))]
