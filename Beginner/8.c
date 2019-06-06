#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const int N = 100;

int ans[100], ans_len = 0;
int cuts[100];
int dp[100][100];
int parent[100][100];

int recur(int l, int r){
    int i, p;
    int bestidx;
    int ret = dp[l][r];
    
    if((l + 1) >= r) return 0;

    if(ret != -1) return ret;
    
    ret = 9999999;
    
    for(i = l + 1; i < r; i++){
        p = recur(l, i) + recur(i, r) + cuts[r] - cuts[l];
        if(p < ret) {
            ret = p;
            bestidx = i;
        }
    }
    parent[l][r] = bestidx;

    return ret;
}

void back(int l, int r){
    if(l+1 >= r)return;

    ans[ans_len++] = cuts[parent[l][r]];

    back(l, parent[l][r]);
    back(parent[l][r], r);
}

void minimiseCost(int N, int *pts, int m) {
    // arr <- {weak points} + {0, N}
    int arr[m + 2], i, j, best;
    int n = m + 2;
    
    arr[0] = 0;
    arr[m + 1] = N;
    
    for(i = 1; i <= m; i++){
        arr[i] = pts[i - 1];
    }

	for(i = 0; i < n; i++)
        cuts[i] = arr[i];

    // intialize all values to -1
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            dp[i][j] =- 1;
        }
    }

    // recursively compute the cost
    best = recur(0, n-1);
 
    // lexographically find the solution points
    back(0, n-1);
}

int main(void){
    int n, m, points[N];
    int i;

    printf("Enter the length of rod: ");
    scanf("%d", &n);
    printf("Enter the number of weak points: ");
    scanf("%d", &m);
    printf("Enter %d weak points: ", m);
    for(i = 0; i < m; i++) scanf("%d", &points[i]); // 0 < points[i]< n

    minimiseCost(n, points, m);

    for(i = 0; i < m; i++) printf("%d\t", ans[i]);
    
    return 0;
}