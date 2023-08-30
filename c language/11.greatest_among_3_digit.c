// file created by : Harsh Raithatha
// file created for finding graetest among 3 digit .....
#include<stdio.h>
int main(){
    int a,b,c;
    
    printf("Enter The Number A : ");
    scanf("%d",&a);
    printf("Enter The Number B : ");
    scanf("%d",&b);
    printf("Enter The Number C : ");
    scanf("%d",&c);

    if (a>b)
    {
        if (a>c)
        {
            printf("A Is Greatest ....");
        }
        else{
            printf("C Is Greatest .....");
        }
        
    }
    else{
        if (b>c)
        {
            printf("B Is Gratest ....");
        }
        else{
            printf("C Is Greatest .....");
        }        
    }

    return 0;
}