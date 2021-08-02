#include <stdio.h>
#include <math.h>

#include "numericalIntegral.h"

float floatTest1(float x){
    return x;
}
double doubleTest1(double x){
    return x;
}

int main(){

    /* Test 1: Integral of y=x at from 1 to 3 */
    printf("Integral of y=x from 1 to 3: float: %f double: %lf\n", FP32RectangleIntegral(floatTest1, 1.0F, 3.0F), FP64RectangleIntegral(doubleTest1, 1.0, 3.0));
    printf("Integral of with simpson method: float: %f double: %lf\n", FP32SimpsonIntegral(floatTest1, 1.0F, 3.0F, FP32Simpson(floatTest1, 1.0F, 3.0F), 1e-6F), FP64SimpsonIntegral(doubleTest1, 1.0, 3.0, FP64Simpson(doubleTest1, 1.0, 3.0), 1e-6));

    /* Test 2: Integral of y=sin(x) from 0 to 2*pi */
    printf("Integral of y=sin(x) from x=0 to x=pi/2 float: %f double: %lf\n", FP32RectangleIntegral(sinf, 0.0, 2.0*M_PI), FP64RectangleIntegral(sin, 0.0, 2.0*M_PI));
    printf("Integral of with adaptive step size method: float: %f double: %lf\n", FP32SimpsonIntegral(sinf, 0.0, 2.0*M_PI, FP32Simpson(sinf, 0.0, 2.0*M_PI), 1e-6F), FP64SimpsonIntegral(sin, 0.0, 2.0*M_PI, FP64Simpson(sin, 0.0, 2.0*M_PI), 1e-6));

    return 0;
}