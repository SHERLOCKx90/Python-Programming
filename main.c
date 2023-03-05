#include <stdio.h>
int foo(int x){
    static int y=7;
    for(int i=1;i<x;i++){
        if((x%(i+y))==0)
        return y--;
    }
    return y++;
}

int main() {
    int y=50;
    printf("%d",foo(y*2));
    printf("\n%d",foo(4));
    printf("\n%d",foo(y));
    printf("\n%d%d",y,foo(70));
    return 0;
}