# https://atcoder.jp/contests/abc135/tasks/abc135_c
import random

N = random.randint(1,100000)
A = [random.randint(1,1000000000) for _ in range(N+1)]
B = [random.randint(1,1000000000) for _ in range(N)]

sum = 0
for j in range(2):
    for i in range(N):
        if A[i + j] < B[i]:
            sum = sum + A[i + j]
            B[i] = B[i] - A[i + j]
            A[i + j] = 0
        elif B[i] < A[i + j]:
            sum = sum + B[i]
            A[i + j] = A[i + j] - B[i]
            B[i] = 0
        elif A[i + j] == B[i]:
            sum = sum + B[i]
            A[i + j] = 0
            B[i] = 0

print(N)
print(sum)