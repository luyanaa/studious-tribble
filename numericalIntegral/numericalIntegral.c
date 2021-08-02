#include <math.h>
float FP32RectangleIntegral(float(*f)(float), float l, float r){
    return (r-l)*f((r+l)/2);
}
float FP32Simpson(float(*f)(float), float l, float r){
    float mid = l+(r-l)/2.0F;
    return (f(l)+4.0F*f(mid)+f(r))*(r-l)/6.0F;
}
float FP32SimpsonIntegral(float(*f)(float), float l, float r, float start, float eps){
    float mid = l+(r-l)/2.0F;
    float L=FP32Simpson(f, l, mid), R=FP32Simpson(f, mid, r);
    if(fabsf(L+R-start)<=15.0F*eps) return (L+R)+(L+R-start)/15.0F;
    else return FP32SimpsonIntegral(f, l, mid, L, eps/2.0F)+FP32SimpsonIntegral(f, mid, r, R, eps/2.0F);
}

double FP64RectangleIntegral(double(*f)(double), double l, double r){
    return (r-l)*f((r+l)/2);
}
double FP64Simpson(double(*f)(double), double l, double r){
    double mid = l+(r-l)/2.0;
    return (f(l)+4.0*f(mid)+f(r))*(r-l)/6.0;
}
double FP64SimpsonIntegral(double(*f)(double), double l, double r, double start, double eps){
    double mid = l+(r-l)/2.0;
    double L=FP64Simpson(f, l, mid), R=FP64Simpson(f, mid, r);
    if(fabs(L+R-start)<=15.0*eps) return (L+R)+(L+R-start)/15.0;
    else return FP64SimpsonIntegral(f, l, mid, L, eps/2.0)+FP64SimpsonIntegral(f, mid, r, R, eps/2.0);
}