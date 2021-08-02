#include <stdio.h>
#include <math.h>

#include "numericalDifferentation.h"

float floatTest1(float x){
    return x;
}
double doubleTest1(double x){
    return x;
}
int main(){

    /* Test 1: Differentation of y=x at x = 0 */
    printf("Differentation of y=x at x=0: float: %f double: %lf\n", FP32gradFinite(floatTest1, 0.0, 1e-6F), FP64gradFinite(doubleTest1, 0.0, 1e-6));
    printf("Differentation of with adaptive step size method: float: %f double: %lf\n", FP32gradAdaptive(floatTest1, 0.0), FP64gradAdaptive(doubleTest1, 0.0));

    /* Test 2: Differentation of y=sin(x) at x=pi/2 */
    printf("Differentation of y=sin(x) at x=pi/2 float: %f double: %lf\n", FP32gradFinite(sinf, M_PI/2.0F, 1e-6F), FP64gradFinite(sin, M_PI/2.0, 1e-6));
    printf("Differentation of with adaptive step size method: float: %f double: %lf\n", FP32gradAdaptive(sinf, M_PI/2.0F), FP64gradAdaptive(sin, M_PI/2.0));

    /* Test 3: Differentation of y=e^x at x=1 */
    printf("Differentation of y=e^x at x=1 float: %f double: %lf\n", FP32gradFinite(expf, 1.0F, 1e-6F), FP64gradFinite(exp, 1.0, 1e-6));
    printf("Differentation of with adaptive step size method: float: %f double: %lf\n", FP32gradAdaptive(expf, 1.0F), FP64gradAdaptive(exp, 1.0));

    return 0;
}