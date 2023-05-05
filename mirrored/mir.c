#include <stdio.h>
#include <string.h>
int main(){
  printf("Ready\n");
  int cont = 0;
  while (cont == 0){
    char pair[10];
    scanf("%[^\n]%*c", pair);
    if (strcmp("qp", pair) == 0){
      printf("Mirrored pair\n");
    } else if (strcmp("pq", pair) == 0){
      printf("Mirrored pair\n");
    } else if (strcmp("db", pair) == 0){
      printf("Mirrored pair\n");
    } else if (strcmp("bd", pair) == 0){
      printf("Mirrored pair\n");
    } else if (strcmp("  ", pair) == 0){
      cont++;
    } else {
      printf("Ordinary Pair\n");
    }
  }
  return 0;
}
