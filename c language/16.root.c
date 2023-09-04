#include <stdio.h>
#include <conio.h>
#include <math.h>

int main() {
    int x,c,n,D,b,a;
    float r1,r2,droot;
    printf("n = a*x^2-b*x+c");
    printf("Enter The value of n : ");
    scanf("%d",&n);

    printf("Enter the value of a : ");
    scanf("%d",&a);

    printf("Enter the value of b : ");
    scanf("%d",&b);

    printf("Enter the value of c : ");
    scanf("%d",&c);

    D = sqrt(pow(b,2)-(4*a*c));
    

    
    float b1,a1,i;
    if ((pow(b,2)-(4*a*c))>= 0)
    {
        r1 = ((-b+sqrt(D))/2*a);
        r2 = ((-b-sqrt(D))/2*a);

    printf(" R1 is : %f \n",r1);

    printf("R2 is : %f",r2);
    }
    else{
        printf("Real roots are not possible");
    }
    
    return 0;
}