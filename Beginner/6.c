#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const int N = 100;

float postFixEval(char *expr){
    float stack[N], a, b;
    int i = 0, top = 0;
    char c;
    int n = strlen(expr);
    while(i < n){
        c = expr[i];
        i++;
        if(c >= 48 && c <= 57){
            stack[top++] = (float)(c - 48);
        }
        else{
            switch (c)
            {
                case '+':
                    b = stack[--top];
                    a= stack[--top];
                    stack[top++] = a + b;
                    break;
                case '-':
                    b = stack[--top];
                    a= stack[--top];
                    stack[top++] = a - b;
                    break;
                case '*':
                    b = stack[--top];
                    a= stack[--top];
                    stack[top++] = a * b;
                    break;
                case '/':
                    b = stack[--top];
                    a= stack[--top];
                    if(b == 0){
                        printf("Division by zero error!\n");
                        exit(0);
                    }
                    stack[top++] = a / b;
                    break;
                default:
                    printf("Invalid expression\n");
                    exit(0);
            }
        }
    }
    return stack[--top];
}

int main(void){
    char exprsn[N];

    printf("Enter the Reverse Polish Expression: ");
    scanf("%s", exprsn);

    printf("Value = %f\n", postFixEval(exprsn));

    return 0;
}