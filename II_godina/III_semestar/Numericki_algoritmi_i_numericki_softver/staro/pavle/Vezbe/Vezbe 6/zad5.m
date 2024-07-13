f = @(x)x.^3.*cos(x);
x = linspace(-pi/2, 5*pi/9);
y = f(x);
plot(x, y, 'r');
hold on;
plot([0 0], [-3 3], 'k');
plot([-2 2], [0 0], 'k');
plot([-2 2], [-0.5 -0.5], 'b');
g = @(x)f(x) + 0.5
[ x, ~ ] = zero_bisection(g, -1.5, -1.25, 10^-5, 100);
scatter(x, f(x), 'b')
x
[ x, ~ ] = zero_bisection(g, -1.25, 0, 10^-5, 100);
scatter(x, f(x), 'b')
x
[ x, ~ ] = zero_bisection(g, 0, 3, 10^-5, 100);
scatter(x, f(x), 'b')
x
