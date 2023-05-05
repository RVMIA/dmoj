#include <stdio.h>

int main(){
  int quarters;
  int first;
  int second;
  int third;
  int plays = 0;

  /*  int constQuarters, constFirst, constSecond, constThird;
  constQuarters = quarters;
  constFirst = first;
  constSecond = second;
  constThird = third; */

  scanf("%d", &quarters);
  scanf("%d", &first);
  scanf("%d", &second);
  scanf("%d", &third);

  while (quarters > 0){
    quarters--;
    plays++;
    first++;
    if (first % 35 == 0){
      quarters += 30;
    }
    if (quarters == 0){
      break;
    }
    quarters--;
    plays++;
    second++;
    if (second % 100 == 0){
      quarters += 60;
    }
    if (quarters == 0){
      break;
    }
    quarters--;
    plays++;
    third++;
    if (third % 10 == 0){
      quarters += 9;
    }
    if (quarters == 0){
      break;
    }
  }
  printf("Martha plays %d times before going broke.\n", plays);
  return 0;
}
