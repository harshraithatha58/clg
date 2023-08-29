// file created by : Harsh Raithatha
// file created for calculator progrmae with if else if and else code ...

#include <stdio.h>

int main(){
    float a, b;
    int c;
    printf("Enter your first number : ");
    scanf("%f", &a);
    printf("Enter your second number : ");
    scanf("%f", &b);
    printf("Enter (1 for +,2 for -,3 for *,4 for / ) : ");
    scanf("%d", &c);

    if (c == 1){
        printf("%f", a + b);
    }
    else if (c == 2){
        printf("%f", a - b);
    }
    else if (c == 3){
        printf("%f", a * b);
    }
    else if (c == 4){
        printf("%f", a / b);
    }
    else{
        printf("Invalid oprator .......");
    }

    return 0;
}