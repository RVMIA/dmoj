#include <stdio.h>
#include <string.h>


char direction[7];
char oppositeDir[7];

int main(){


	int extNum;

	scanf("%d", &extNum);
	scanf("%s", direction);


	if(strlen(direction) == 5){
		strcpy(oppositeDir, "left\n");
	} else {
		strcpy(oppositeDir, "right\n");
	}



	if (extNum % 2 == 0){
		printf("%s\n", oppositeDir);
	} else {
		printf("%s\n", direction);
	}

	return 0;
}
