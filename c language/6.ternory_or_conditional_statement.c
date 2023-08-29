#include<stdio.h>


int main(){
    int a,b,max;

    printf("Enter the number one : ");
    scanf("%d",&a);

    printf("Enter the number two : ");
    scanf("%d",&b);

    max = a>b ? a:b;

    printf("The Bigger digit is %d ",max);

    return 0;

}