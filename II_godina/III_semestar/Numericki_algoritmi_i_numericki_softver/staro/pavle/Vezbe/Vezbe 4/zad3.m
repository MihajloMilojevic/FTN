f = @(x) sin(2*x);

x = linspace(pi/3, 7*pi/3, 1000);

fx = f(x);

plot(x, fx, 'blue'), hold on

plot([1 8.5], [0 0], 'k'), hold on

[x, y] = zero_bisection(f, pi/3, 2*pi/3, 10^-3, 100);
plot(x, y, 'red*')
plot([pi/3 pi/3], [10 -10], 'red')
plot([2*pi/3 2*pi/3], [10 -10], 'red')

[x, y] = zero_bisection(f, 2*pi/3, 4*pi/3, 10^-3, 100);
plot(x, y, 'red*')

plot([4*pi/3 4*pi/3], [10 -10], 'red')

[x, y] = zero_bisection(f, 4*pi/3, 5*pi/3, 10^-3, 100);
plot(x, y, 'red*')

plot([5*pi/3 5*pi/3], [10 -10], 'red')

[x, y] = zero_bisection(f, 5*pi/3, 7*pi/3, 10^-3, 100);
plot(x, y, 'red*')

