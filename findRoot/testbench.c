#include <stdio.h>
#include <math.h>

#include "findRoot.h"

float floatTest1(float x){
    return x*x+2.0*x-3;
}

int main(){

    printf("Root of f(x)=x^2+2x-3: \n");
    printf("Newton Method: %f\n", FP32newtonMethod(floatTest1, 2.5F));

    printf("Root of f(x)=sin(x) \n");
    printf("Divide and Conquer Method: %f\n", FP32divideMethod(cosf, 0, M_PI, 1e-5F));
    return 0;
}