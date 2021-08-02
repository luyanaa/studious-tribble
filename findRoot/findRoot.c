#include <math.h>
#include <assert.h>
#include <stdio.h>
float FP32gradAdaptive(float(*f)(float), float x){
    float h, xph, dx, slope;
    h = sqrtf(__FLT_EPSILON__)*x; 
    xph = x+h;
    dx = xph-x;
    slope = (f(xph)-f(x))/h;
    return slope;
}


float FP32newtonMethod(float (*f)(float), float x){
    const float step=1e-5F;
    float x0, h;
    do{
        x0 = x;
        h = f(x)/FP32gradAdaptive(f, x);
        x = x0 - h;
    }while(fabsf(x-x0)>=step);
    return x;
}

float FP32divideMethod(float (*f)(float), float l, float r, float eps){
    /* Assuming f(l)*f(r)<0 */
    float mid = (l+r)/2.0F, err=f(mid);
    assert(f(l)*f(r)<0);
    while(err>eps){
        if(f(l)*f(mid)>0.0)
            l=mid;
        else 
            r=mid;
        mid = (l+r)/2.0F;
        err = f(mid);
    }
    return mid;
}
