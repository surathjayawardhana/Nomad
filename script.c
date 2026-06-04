#include <stdio.h>

int main() {
    int x = 10;
    printf("Hello World!\n");
    printf("Value of x is: %d\n", x);

    for (int i = 1; i <= 4; i++) {
        for (int j = -1; j < i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 4 - i; j++) {
            printf(" ");
        }
        for (int k = 0; k < i + 1; k++) {
            printf("*");
        }
        printf("\n");
    }

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 2 - i; j++) {
            printf(" ");
        }
        for (int k = 0; k < i + 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    getchar();
    return 0;
}

