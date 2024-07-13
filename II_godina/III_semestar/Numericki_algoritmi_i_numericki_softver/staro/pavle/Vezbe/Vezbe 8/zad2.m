f = @(x) exp(-x.^2/ 2);
a = 0;
b = 0.2;
I = 2/sqrt(2*pi)*integrateSimpson(f, a, b, 100, 10)
