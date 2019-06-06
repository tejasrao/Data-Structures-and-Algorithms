#include<stdio.h>
#include<stdlib.h>

const int N = 100;

int max(int a, int b){
    return (a > b)?a:b;
}

int main(void){
    int n, arr[N], currentSum, maxSum;
    int i;
    
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    printf("Enter %d elements: ", n);
    for(i = 0; i < n; i++) scanf("%d", &arr[i]);
    
    // Kadane's algorithm
    currentSum = arr[0];
    maxSum = arr[0];
    for(i = 1; i < n; i++){
        currentSum = max(arr[i], currentSum+arr[i]);
        maxSum = max(maxSum, currentSum);
    }
    
    printf("Maximum subarray sum = %d\n", maxSum);

    return 0;
}