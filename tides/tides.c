#include <stdio.h>

int main(){
  int num;
  scanf("%d", &num);
  int measurements[num];
  int low[num/2+1];
  int high[num/2];
  for (int i = 0; i < num; i++){
    scanf("%d", &measurements[i]);
  }
  low[0] = measurements[0];
  high[0] = measurements[1];
  for (int i = 0; i < (sizeof(low)/sizeof(low[0])); i++){
    printf("%d\t%d\n", i, low[i]);
  }
  for (int i = 0; i < (sizeof(high)/sizeof(high[0])); i++){
    printf("%d\t%d\n", i, low[i]);
  }
  return 0;
}
