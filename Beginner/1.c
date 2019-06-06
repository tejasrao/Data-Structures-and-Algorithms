#include <stdio.h>
#include <stdlib.h>
const int ROWS = 100;
const int COLS = 100;

void printMatrix(int mat[ROWS][COLS], int r, int c) {
    int i, j;

    printf("\n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}


void rotateMatrix(int mat[ROWS][COLS], int r, int c) {
    int i, j;
    int temp;

    for (i = 0; i < r; i++) {
        for (j = i; j < c; j++) {
            if(i != j){
            mat[i][j] = (mat[i][j] + mat[j][i]);
            mat[j][i] = (mat[i][j] - mat[j][i]);
            mat[i][j] = (mat[i][j] - mat[j][i]);
            }
        }
    }

    for (i = 0; i < c; i++) {
        for (j = 0; j < (int)(r / 2); j++) {
            mat[i][j] = mat[i][j] + mat[i][r - j - 1];
            mat[i][r - j - 1] = mat[i][j] - mat[i][r - j - 1];
            mat[i][j] = mat[i][j] - mat[i][r - j - 1];
        }
    }
}


int main(void) {
    int matrix[ROWS][COLS];
    int r, c;
    int i, j;

    printf("Enter the number of rows: ");
    scanf("%d", & r);
    printf("Enter the number of columns: ");
    scanf("%d", & c);

    printf("Enter the matrix values: \n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            scanf("%d", & matrix[i][j]);
        }
    }

    printf("Matrix before rotation\n");
    printMatrix(matrix, r, c);

    rotateMatrix(matrix, r, c);

    printf("Matrix after rotation\n");
    printMatrix(matrix, c, r);

    return 0;
}