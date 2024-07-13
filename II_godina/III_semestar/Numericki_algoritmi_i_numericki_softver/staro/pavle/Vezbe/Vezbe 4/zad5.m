h = @(x)2*x.^2-4;

x = linspace(-2, 2, 1000);

y = h(x);

plot(x, y, 'blue'), hold on

plot([-5 5], [0 0], 'k'), hold on
plot([0 0], [-5 5], 'k')

[x y] = zero_bisection(h, -2, 0, 10^-3, 1000)
plot(x, y, 'green*')

[x y] = zero_bisection(h, 0, 2, 10^-3, 1000)
plot(x, y, 'green*')