#include <stdio.h>
#include <string.h>

int main(){
  int len, index;
  int j = 1;
  char word[80];
  scanf("%d", &len);
  for (int i = 0; i < len; i++){
    scanf("%d %[^\n]%*c", &index, word);
    printf("%d ", j);
    for (int i = 0; i < strlen(word); i++){
      if (i != index-1){
	printf("%c", word[i]);
      }
    }
    printf("\n");
    j++;
  }
  return 0;
}


