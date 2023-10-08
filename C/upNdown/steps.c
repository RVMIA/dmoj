#include <stdio.h>
int steps(int forward, int backward, int steps){
  int sum = 0;
  int s = forward + backward;
  for (int i = 0; sum < steps; i++){
    sum += s;
  }
  int total = steps+sum;
  int arr[total];
  long ind = 0;
  int out = 0;
  while (ind < steps){
    for (int i = 0; i < (forward); i++){
      arr[ind] = 1;
      ind += 1;
    }
    for (int i = 0; i < (backward); i++){
      arr[ind] = -1;
      ind += 1;
    }
    /* for (int i = 0; i < steps; i++){
      printf("%d\t", arr[i]);
      }*/
  }
    for (int i = 0; i < steps; i++){
      if (arr[i] == 1){
	out++;
      }
      if (arr[i] == -1){
	out--;
      }
    }
  return out;
  
}
int main(){
  int a, b, c, d, s;
  int pNikky = 0;
  int pByron = 0;
  scanf("%d\n%d\n%d\n%d\n%d", &a, &b, &c, &d, &s);
  pNikky = steps(a, b, s);
  pByron = steps(c, d, s);
  // printf("Nikky: %d\nByron: %d\n", pNikky, pByron);
  if (pNikky > pByron){
    printf("Nikky\n");
  } else if (pByron > pNikky){
    printf("Byron\n");
  } else if (pNikky == pByron){
    printf("Tied\n");
  }
  return 0;
}
