h = @(x)sin(2*x) - x;
dh = matlabFunction(diff(sym(h)))
x = linspace(0, 2*pi, 1000);

y = dh(x);
z = h(x);

plot(x, z, 'blue'), hold on

plot([0 2*pi], [0 0], 'k'), hold on
plot([0 0], [-5 5], 'k')

[x y] = zero_bisection(dh, 0, pi/4, 10^-4, 100000)
plot(x, h(x), 'green*')
plot(x, y, 'red*')

[x y] = zero_bisection(dh, pi/4, pi, 10^-4, 100000)
plot(x, h(x), 'green*')
plot(x, y, 'red*')

[x y] = zero_bisection(dh, 3*pi/2, 2*pi, 10^-4, 100000)
plot(x, h(x), 'green*')
plot(x, y, 'red*')