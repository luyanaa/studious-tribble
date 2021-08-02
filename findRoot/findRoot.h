float FP32gradFinite(float(*f)(float), float x, float delta);
float FP32newtonMethod(float (*f)(float), float x);
float FP32divideMethod(float (*f)(float), float l, float r, float eps);