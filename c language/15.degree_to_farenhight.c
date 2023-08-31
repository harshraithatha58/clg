// file created by : Harsh Raithatha
// file created for degree to farenhight and farenhight to degree
// formula by f : f = (9/5)*c+32
// formula by c : c = (5(f-32))/9

#include<stdio.h>
int main(){

    float C,F;
    int O;

    printf("Enter 1 For Degree Celcius to Farenhight ... \n");
    printf("Enter 2 For Degree Farenhight to Degree Celcius ...\n");
    printf("\n");
    printf("Enter Your selection Frome Above : ");
    scanf("%d",&O);

    if (O == 1)
    {
        printf("Enter The Degree Celcius : ");
        scanf("%f",C);

        F = (9/5)*C+32;

        printf("The degree Farenheight is : %f",F);

    }
    else{
        printf("Enter The Degree Farenhight : ");
        scanf("%f",&C);

        C = (5*(F-32))/9;
        printf("The degree Celcius is : %f",C);
    }
    

    return 0; 
}
