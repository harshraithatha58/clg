#include<stdio.h>
int main(){
    int n,reversed=0,orignal,remainder;
    printf("Enter a number : ");
    scanf("%d",&n);

    orignal = n;
    while (n!=0)
    {
        remainder = n%10;
        reversed = reversed*10 + remainder;
        n = n/10;
    }
    

    return 0;
}