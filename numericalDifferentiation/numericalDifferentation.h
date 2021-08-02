
double FP64gradFinite(double(*f)(double), double x, double delta);
float FP32gradFinite(float(*f)(float), float x, float delta);

double FP64gradAdaptive(double(*f)(double), double x);
float FP32gradAdaptive(float(*f)(float), float x);
