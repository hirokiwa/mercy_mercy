#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){

    int player[2];
    srand((unsigned int)time(NULL));

    for(int i=0; i<2; i++){

        int score = 0;
        
        int board[10] ={0};
        for(int j=0; j<10; j++){
            int ball, n;

            n = rand();

            ball = n % 20; //0~19

            if((ball > 0) && (ball < 10)){
              board[ball] = 1;
            }
        }

        for(int j=1; j<10; j++){
            if(board[j] == 1){
                score += j;
            }
        }

        player[i] = score;

    }

    printf("りゅうのすけ：%d点\n", player[0]);
    printf("しゅんき：%d点\n", player[1]);

    if(player[0] > player[1]){
        puts("りゅうのすけの勝ち");
    }else if(player[1] > player[0]){
        puts("しゅんきの勝ち");
    }else{
        puts("引き分け");
    }

    return(0);
}