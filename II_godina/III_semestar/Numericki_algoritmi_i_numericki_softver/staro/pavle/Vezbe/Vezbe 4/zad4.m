h = @(x)x.^2-x+3-exp(x);

x = linspace(0, 2, 1000);

y = h(x);

plot(x, y, 'red'), hold on

plot([0 10], [0 0], 'k'), hold on

[x y] = zero_bisection(h, 0, 2, 10^-4, 100)

plot(x, y, 'green*')

