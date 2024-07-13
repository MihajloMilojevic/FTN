f = @(x)sin(x);
a = 0;
b = 3*pi/2;
intervals = 4;
x = linspace(a, b, 100);
plot(x, f(x), 'blue', [a b], [0 0], 'black'), hold on;
%I = integrateTrapezoid(f, a, b, 20, 10)
I = integrateSimpson(f, a, b, 10, 10)