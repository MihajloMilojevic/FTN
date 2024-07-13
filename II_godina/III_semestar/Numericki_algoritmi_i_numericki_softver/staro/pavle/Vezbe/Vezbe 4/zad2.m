f = @(x) cos(x);

x = linspace(pi/3, 4*pi/3, 1000);

fx = f(x);

plot(x, fx, 'blue'), hold on

plot([1 4.5], [0 0], 'k'), hold on

[x, y] = zero_bisection(f, pi/3, 4*pi/3, 10^-3, 100);

plot(x, y, 'red*')