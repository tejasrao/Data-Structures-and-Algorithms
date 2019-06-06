#include<stdio.h>
#include<stdlib.h>
#include<math.h>

const int N = 100;

int max(int a, int b){
    return (a > b)?a:b;
}

void bubbleSort(int* a, int n){
    int i, j;
    for(i = 0; i < n - 1; i++){
        for(j = i + 1; j < n - i - 1; i++){
            if(a[i] > a[j]){
                a[i] ^= a[j];    
                a[j] ^= a[i];    
                a[i] ^= a[j];    
            }
        }
    }
}

int minimalTime(int n, int boards[], int k, int painters[]){
    int i, j;
    int total = 0, currentValue, product;
    int sum[k];
    
    for(i = 0; i < k; i++) sum[i] = 0;

    sum[k - 1] = ceil(boards[n - 1] / painters[k - 1]);
    currentValue = ceil(boards[n - 1] / painters[k - 1]);

    for(i = k - 2, j = n - 2; i >= 0 && j >= 0; j--){
        product = ceil(boards[j] / painters[i]);
        if(product <= currentValue){
            sum[i] += product;
            currentValue = product;
            total = max(total, sum[i]);
            i--;
        } else{
            sum[i + 1] +=  ceil(boards[j] / painters[i + 1]);
            currentValue = ceil(boards[j] / painters[i + 1]);
            total = max(total, sum[i + 1]);
        }
    }
    return total;
}

int main(void){
    int n, boards[100] = { 0 }, k, painters[100];
    int i, j;

    printf("Enter the number of boards: ");
    scanf("%d", &n);
    printf("Enter length of %d boards: ", n);
    for(i = 0; i < n; i++) scanf("%d", &boards[i]);
    printf("Enter the number of painters: ");
    scanf("%d", &k);
    printf("Enter time-rate of %d painters: ", k);
    for(i = 0; i < k; i++) scanf("%d", &painters[i]);

    // sort boards and painters
    bubbleSort(boards, n);
    bubbleSort(painters, k);
    printf("Minimum time = %d\n", minimalTime(n, boards, k, painters));

    return 0;   
}