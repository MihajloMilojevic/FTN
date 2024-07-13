f = @(x)x.^2.*sin(x);
x = linspace(-pi, pi, 1000);
y = f(x);
plot(x, y, 'r');
hold on;
plot([-5 5], [0 0], 'k');
plot([0 0], [-5 5], 'k');
p = lsquares(x, y, 3);
g = @(x)polyval(p, x);
z = g(x);
plot(x, z, 'b');
h = @(x)f(x)-g(x);
[x y]= zero_bisection(h, -1/2, 1/2, 10^-8, 100);
scatter(x, y, 'g*');

