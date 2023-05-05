#include <stdio.h>

int main () {
    int input1, input2, square;
    float circle;

    scanf("%i",&input1);
    scanf("%i",&input2);

    square = input1*input1;
    circle = (input2*input2)*3.14159;
    
    if (square<circle) {
        printf("CIRCLE");
    } else {
        printf("SQUARE");
    }
    
    return 0;

}
