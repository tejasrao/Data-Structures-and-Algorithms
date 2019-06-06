#include<stdio.h>
#include<stdlib.h>

const int N = 100;

int subSeq(int *arr, int n) {
    int i, j;
    int count[n], max = 1;
    count[0] = 1;

    for(i = 1; i < n; i++) {
        count[i] = 1;
        for(j = 0; j < i; j++) {
            if(arr[i] > arr[j] && count[i] < (count[j] + 1))
                count[i] = count[j] + 1;
        }
        max = (max > count[i]) ? max : count[i];
    }

    return max;
}

int main(void) {
    int arr[N], n;
    int i;

    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for(i = 0; i < n; i++) scanf("%d", &arr[i]);

    printf("Longest Increasing Subcountuence: %d\n", subSeq(arr, n));
    
    return 0;
}