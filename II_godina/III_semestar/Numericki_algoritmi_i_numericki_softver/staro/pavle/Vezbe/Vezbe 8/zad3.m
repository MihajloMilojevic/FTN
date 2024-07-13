clc;

f = @(x) x.^2 ;
g = @(x) sqrt(x);
h = @(x) g(x) - f(x);

x = linspace(-1, 3, 100);
plot(x, f(x), 'b'), hold on;
plot(x, g(x), 'r');
I = 0;
I1 = integrateSimpson(f, 0, 1, 100, 0);
I2 = integrateSimpson(g, 0, 1, 100, 0);
I = I + I2 - I1;
I3 = integrateSimpson(f, 1, 2, 100, 0);
I4 = integrateSimpson(g, 1, 2, 100, 0);
I = I + I3 - I4
