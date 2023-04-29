#include <stdio.h>
#include <string.h>
   
int main () {
    
    char *letter;
    int cases, tcount = 0, scount = 0;
    
    scanf("%d", &cases);
    
    for(int i = 0; i < cases;){
        scanf("%c", letter);
        if (strcmp(letter, ".") == 0 || strcmp(letter, "?") == 0 || strcmp(letter, "!") == 0){
            i++;
        } else if (strcmp(letter, "s") == 0 || strcmp(letter, "S") == 0) {
            scount += 1;
        } else if (strcmp(letter, "t") == 0 || strcmp(letter, "T") == 0) {
            tcount += 1;
        }
    }
   
    printf("%d\t%d", scount, tcount);
    
    return 0;
}