f = @(x) exp(x) + 2;
g = @(x) sqrt(x);

f2 = @(x) f(x).^2;
g2 = @(x) g(x).^2;

x = linspace(1, 4, 100);
plot(x, f(x), 'b'), hold on;
plot(x, g(x), 'r');

I1 = pi*integrateSimpson(f2, 2, 3, 100, 0);
I2 = pi*integrateSimpson(g2, 2, 3, 100, 0);
I = I1 - I2