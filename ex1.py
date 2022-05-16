import random

player = [0] *2

for i in range(2):
    score = 0
    board = [False]*9

    for j in range(10):
        ball = random.randint(0,20) 
        if (ball < 9):
            board[ball] = True

    for j in range(9):
        if board[j] == True:
            score += (j + 1)
    
    player[i] = score

print("りゅうのすけ："+str(player[0]))
print("しゅんき："+str(player[1]))

if(player[0] > player[1]):
    print("りゅうのすけの勝ち")
elif(player[1] > player[0]):
    print("しゅんきの勝ち")
else:
    print("引き分け")