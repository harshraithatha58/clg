//file created by : Harsh Raithatha
//file created for making right angle triangle by  1234
#include<stdio.h>
int main(){

    int row = 5;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("%d",j+1);
        }
        printf("\n");
        
    }
    

    return 0;
} 