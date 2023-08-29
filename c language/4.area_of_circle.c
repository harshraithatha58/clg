//File Created By : Harsh Raithatha 
// file created for finding the area of circle 
#include<stdio.h>
#define pi 3.1415
int main(){
    float r,res;
    printf("Enter The Radius of Circle : ");

    scanf("%f",&r);

    res = pi*r*r;

    printf("area of circle is : %f",res);
    return 0;
}