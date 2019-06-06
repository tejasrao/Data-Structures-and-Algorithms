#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const int N = 100;

int min(int x, int y){
    return (x < y)? x : y;
}

int findMinOps(int n, char *a, int m, char *b){
    int costMatrix[n + 1][m + 1]; // operations count - overlapping subproblems(dp)
    int i, j;
    
    for(i = 0; i <= n; i++){
        for(j = 0; j <=n; j++){
            if(i == 0) costMatrix[i][j] = j;
            else if(j == 0) costMatrix[i][j] = i;
            else if(a[i - 1] == b[j - 1]) costMatrix[i][j] = costMatrix[i - 1][j - 1];
            else costMatrix[i][j] = 1 + min(costMatrix[i - 1][j - 1], min(costMatrix[i][j - 1], costMatrix[i - 1][j])); 
        }
    }

    return costMatrix[n][m];
}

int main(void){
    char A[N], B[N];

    printf("Enter the first string: ");
    scanf("%s", A);
    printf("Enter the second string: ");
    scanf("%s", B);

    printf("Minimum number of operations = %d\n", findMinOps(strlen(A), A, strlen(B), B));

    return 0;
}