#include<stdio.h>
#include<stdlib.h>

struct node {
    struct node *right;
    struct node *left;
    int value;
};

typedef struct node Node;

Node* newNode(int value) {
    Node *node =  (Node*)malloc(sizeof(Node));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void printArray(int *a, int n) {
    int i;
    printf("\nPath:\t");
    for(i = 0; i < n; i++){
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void traversePath(Node* node, int *path, int n, int sum) {
    int subSum;
    
    if(node == NULL){
        if(sum == 0) 
            printArray(path, n);
        return;
    }
    
    path[n++] = node->value;
    subSum = sum - node->value;

    if(subSum == 0 && node->left == NULL && node->right == NULL) {
            printArray(path, n);
    } else {
        if(node->left) {
            traversePath(node->left, path, n, subSum);
        }
        if(node->right) {
            traversePath(node->right, path, n, subSum);
        }
    }
}

void findPaths(Node* node, int sum) {
    int path[100];
    traversePath(node, path, 0, sum);
}

int main(void){
    int sum;
    Node *root = newNode(2);
    root->left = newNode(5);
    root->right = newNode(10);
    root->left->left = newNode(1);
    root->left->right = newNode(7);
    root->right->left = newNode(6);
    root->right->right = newNode(2);
    
    printf("Enter sum: ");
    scanf("%d", &sum);

    findPaths(root, sum);

    return 0;
}