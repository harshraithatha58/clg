#include<stdio.h>

int main(){
    int c;
    int a,b;
    printf("Enter your first number : ");
    scanf("%d",&a);
    printf("Enter your second number : ");
    scanf("%d",&b);
    printf("Enter (1 for +,2 for -,3 for *,4 for / ) : ");
    scanf("%d",&c);

    switch(c){
    case 1:
        printf("Addition is %d",a+b);
        break;
    
    case 2:
        printf("sub is %d",a-b);
        break;
    
    case 3:
        printf("multiply is %d",a*b);
        break;
    
    case 4:
        printf("division is %d",a/b);
        break;
    

    
    default:
        printf("wrong input entered.....");
        break;
    }
    
    return 0;
}