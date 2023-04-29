#include <stdio.h>

int main () {

    int cases, A, B, P;

    scanf("%d",&cases);
    for (int i = 0; i < cases; i++) {
        scanf("%d %d %d",&A,&B,&P);
        if (A * B == P){
            printf("POSSIBLE DOUBLE SIGMA\n");
        } else {
            printf("16 BIT S/W ONLY\n");
        }
    }
    






    return 0;
}