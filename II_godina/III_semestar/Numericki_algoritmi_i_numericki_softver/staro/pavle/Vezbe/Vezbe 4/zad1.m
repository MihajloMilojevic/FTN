f = @(x) sin(x);
df = matlabFunction(diff(sym(f)))
x = linspace(pi/3, 4*pi/3, 1000);

fx = f(x);

plot(x, fx, 'blue'), hold on

plot([1 8], [0 0], 'k'), hold on

[x, y] = zero_bisection(f, pi/3, 4*pi/3, 10^-3, 100);
[x, y] = newton(f, df, 4*pi/3, 10^-3, 100);
[x, y] = secica(f, pi/3, 4*pi/3, 10^-3, 100);
[x, y] = regula_falsi(f, pi/3, 4*pi/3, 10^-3, 100);
plot(x, y, 'red*')
