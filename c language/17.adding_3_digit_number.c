#include <stdio.h>

int main()
{
    int user_input, remainder, sum = 0, temp;

    printf("Enter The 3 digit number : ");
    scanf("%d", &user_input);
    temp = user_input;
    while (user_input != 0)
    {
        remainder = user_input % 10;
        user_input = (user_input - remainder) / 10;
        sum = sum + remainder;
    }
    printf("%d", sum);

    return 0;
}