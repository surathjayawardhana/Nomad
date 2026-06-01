#include <stdio.h>

int main() {
    printf("\nHello world!\n");

    int no;
    printf("\nEnter a question number: ");
    scanf("%d", &no);

    if (no == 1) {

        printf("\nQuestion 1: Swap two numbers\n");

        int num1, num2;

        printf("\nEnter first number: ");
        scanf("%d", &num1);

        printf("Enter second number: ");
        scanf("%d", &num2);

        printf("\nBefore swapping: %d, %d\n", num1, num2);

        int y = num1;
        num1 = num2;
        num2 = y;

        printf("After swapping: %d, %d\n", num1, num2);
    }

    else if (no == 2) {

        printf("\nQuestion 2: Find the maximum of two numbers\n");

        float num3, num4;

        printf("\nEnter first number: ");
        scanf("%f", &num3);

        printf("Enter second number: ");
        scanf("%f", &num4);

        if (num3 == num4){
            printf("\n%.2f and %.2f are equal", num3, num4);
        }
        else if (num3 > num4){
            printf("\n%.2f = Maximum number", num3);
        }
        else{
            printf("\n%.2f = Maximum number", num4);
        }
    }

    else if (no == 3) {
        printf("\nQuestion 3: Check if a number is positive or negative\n");

        int num5;

        printf("\nEnter a number: ");
        scanf("%d", &num5);

        if (num5 >= 0){
            printf("\n%d is a positive number", num5);
        }
        else{
            printf("\n%d is a negative number", num5);  
        }
    }

    else if (no == 4) {
          printf("\nQuestion 4: Check if a student has passed or failed\n");
          int num6;
          printf("\nEnter your marks: ");
          scanf("%d", &num6);
          if (num6 >= 50){
            printf("\nPassed");
          }
          else{
            printf("\nFailed");
        }
    }

    else if (no ==5){
            printf("\nQuestion 5: Check if a person is eligible to vote\n");

            int age;
            printf("\nEnter your age: ");
            scanf("%d", &age);

            if (age >= 18){
                printf("\nYou are eligible to vote");
            }
            else{
                printf("\nYou are not eligible to vote");
            }

    }
    else if (no ==6){
        printf("\nQuestion 6: Check if a number is even or odd\n");
        int num7;
        printf("\nEnter a integer: ");
        scanf("%d", &num7);
        if (num7 % 2 == 0){
            printf("\n%d is an even number", num7);
        }
        else{
            printf("\n%d is an odd number", num7);
        }
    }
    else if (no ==7){
        printf("\nQuestion 7: Check if a number is positive, negative or zero\n");
        int num8;
        printf("\nEnter a integer: ");
        scanf("%d", &num8);
        if (num8 > 0){
            printf("\n%d is a positive number", num8);
        }
        else if (num8 < 0){
            printf("\n%d is a negative number", num8);
        }
        else{
            printf("\n%d is zero", num8);
        }
    }

    else if (no ==8){
        printf("\nQuestion 8: Find the largest of three numbers\n");
        int num9,num10,num11;
        printf("\nEnter first number: ");
        scanf("%d", &num9);
        printf("Enter second number: ");
        scanf("%d", &num10);
        printf("Enter third number: ");
        scanf("%d", &num11);

        if (num9 >= num10 && num9 >= num11){
            printf("\n%d is the largest number", num9);
        }
        else if (num10 >= num9 && num10 >= num11){
            printf("\n%d is the largest number", num10);
        }
        else{
            printf("\n%d is the largest number", num11);
        }
    }
    else{
        printf("\nInvalid question number");
    }
    getchar();
    getchar();
    return 0;
}
