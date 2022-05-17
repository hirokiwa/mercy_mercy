import random

check = [[0 for _ in range(2)] for _ in range(40)]
bingo = [False for _ in range(2)]

def make_sheet():
    sheet = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(2)]
    
    for i in range(2):

        ran = [0]*9

        cnt = 0
        while ran[8] == 0:
            n = random.randint(1,40)
            if not n in ran:
                ran[cnt] = n
                cnt += 1

        for j in range(3):
            for k in range(3):
                n = ran[3 * j + k]
                sheet[i][j][k] = n
                check[n-1][i] = [j,k]

    return sheet

def check_bingo(sheet):
    bingo = False

    for i in range(2):
        # ヨコ
        for j in range(3):
            if sheet[j][0] == sheet[j][1] == sheet[j][2]:
                bingo = True
                return bingo

        # タテ
        for j in range(3):
            if sheet[0][j] == sheet[1][j] == sheet[2][j]:
                bingo = True
                return bingo

        # ナナメ
        if sheet[0][0] == sheet[1][1] == sheet[2][2]:
            bingo = True
        elif sheet[2][0] == sheet[1][1] == sheet[0][2]:
            bingo = True

    return bingo

# ビンゴカード発行
sheet = make_sheet()

for i in range(3):
    print(str(sheet[0][i])+"    "+str(sheet[1][i]))
print("\n")

while not True in bingo:
    ran_num = random.randint(1,40)
    if check[ran_num - 1] != [0,0]:
        for i in range(2):
            if check[ran_num - 1][i] != 0:
                sheet[i][check[ran_num - 1][i][0]][check[ran_num - 1][i][1]] = 0
                bingo[i] = check_bingo(sheet[i])

print("結果")
for i in range(3):
    print(str(sheet[0][i])+"    "+str(sheet[1][i]))

if bingo[0] == bingo[1]:
    print("引き分け")
elif bingo[0] == True:
    print("Aの勝ち")
else:
    print("Bの勝ち")