#include<stdio.h>
#include<stdlib.h>

const int N = 100;

int find(int set[], int value, int n){
    int i;
    for(i = 0 ; i < n; i++){
        if(set[i] == value)
            return i;
    }
    set[i] = value;
    return -1;
}

int main(void){
    int nodes[N];
    int n, i, set[N], len = 0;
    
    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    printf("Enter the value of %d nodes: ", n);
    for(i = 0; i < n; i++){
        scanf("%d", &nodes[i]);
    }

    for(i = 0; i < n; i++){
        if(find(set, nodes[i], len) < 0){
            len++;
        } else {
            printf("Loop detected!\n");
            exit(0);
        }
    }

    printf("No Loop detected!\n");

    return 0;
}