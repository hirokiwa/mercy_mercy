# https://atcoder.jp/contests/abc135/tasks/abc135_b

import random
import sys

N = random.randint(2,50)
p = [i + 1 for i in range(N)]

def check(p):
    for i in range(N):
        if p[i] != i + 1:
            return
    print("YES")
    sys.exit()
    
for i in range(N):
    target_a = random.randint(0, N - 1)
    target_b = random.randint(0, N - 1)
    temp = p[target_a]
    p[target_a] = p[target_b]
    p[target_b] = temp

print(p)

i = random.randint(1,N)
j = i

while i == j:
    j = random.randint(1,N)

if i > j:
    temp = i
    i = j
    j = temp

check(p)

temp = p[i - 1]
p[i - 1] = p[j - 1]
p[j - 1] = temp

print(p)
check(p)

print("NO")


