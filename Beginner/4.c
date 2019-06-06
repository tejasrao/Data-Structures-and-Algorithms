#include<stdio.h>
#include<stdlib.h>

const int N = 100;

int main(void){
    int n, arr[N], i, j;
    int A = -1, B = -1;

    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    printf("Enter %d elements: ", n);
    for(i = 1; i <= n; i++) scanf("%d", &arr[i]);

    for(i = 1; i <= n; i++){
        j = abs(arr[i]);
        if(arr[j] > 0){
            arr[j] = -arr[j];
        } else {
            A =abs(arr[i]);
        }
        if(arr[i] > 0){
            B = i;
        }
    }
    
    printf("A = %d;\tB = %d\n", A, B);

    return 0;
}