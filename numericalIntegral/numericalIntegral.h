float FP32RectangleIntegral(float(*f)(float), float l, float r);
float FP32SimpsonIntegral(float(*f)(float), float l, float r, float start, float eps);
float FP32Simpson(float(*f)(float), float l, float r);

double FP64RectangleIntegral(double(*f)(double), double l, double r);
double FP64SimpsonIntegral(double(*f)(double), double l, double r, double start, double eps);
double FP64Simpson(double(*f)(double), double l, double r);