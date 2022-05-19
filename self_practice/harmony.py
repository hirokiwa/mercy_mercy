# https://atcoder.jp/contests/abc135/tasks/abc135_a
import random

A = random.randint(-1000000000,0)
B = A

while A == B:
    B = random.randint(-100000000,100000000)

print("A="+str(A))
print("B="+str(B))

if A > B:
    temp = A
    A = B
    B = temp

if (B - A) % 2 == 0: 
    K = (B - A) / 2
    print(int(K))
else:
    print("IMPOSSIBLE")