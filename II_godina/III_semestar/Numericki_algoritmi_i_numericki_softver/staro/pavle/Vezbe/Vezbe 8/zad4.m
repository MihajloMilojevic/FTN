f = @(x) exp(x.*2)/x;
a = 1;
b = 2;
g = @(x) f(x).^2;
I = pi*integrateSimpson(g, 1, 2, 100, 0)