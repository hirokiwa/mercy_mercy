print("第n項までのフィボナッチ数列の和を計算します")

n = 0

while (n <= 0):
    print("n=")
    n = int(input())

num_rear = 0
num = 1

sum = 0

for i in range(n):
    sum += num
    temp = num_rear
    num_rear = num
    num = temp + num

print("第"+str(n)+"項項までの合計は"+str(sum))