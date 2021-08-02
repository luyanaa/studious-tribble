#include <math.h>

double FP64gradFinite(double(*f)(double), double x, double delta){
    return (f(x+delta)-f(x-delta))/(2.0*delta);
}


float FP32gradFinite(float(*f)(float), float x, float delta){
    return (f(x+delta)-f(x-delta))/(2.0*delta);
}

double FP64gradAdaptive(double(*f)(double), double x){
    double h, xph, dx, slope;
    h = sqrt(__DBL_EPSILON__)*x; 
    xph = x+h;
    dx = xph-x;
    slope = (f(xph)-f(x))/h;
    return slope;
}

float FP32gradAdaptive(float(*f)(float), float x){
    float h, xph, dx, slope;
    h = sqrtf(__FLT_EPSILON__)*x; 
    xph = x+h;
    dx = xph-x;
    slope = (f(xph)-f(x))/h;
    return slope;
}
