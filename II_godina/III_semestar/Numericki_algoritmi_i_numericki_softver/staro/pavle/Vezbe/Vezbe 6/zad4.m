x = [0 1 2 3 4 5];
y = [5 3 5 1 3 5];
scatter(x, y, 'r');
hold on;
p = lsquares(x, y, 5);
f = @(x)polyval(p, x);
xx = linspace(0, 5.5, 1000);
plot(xx, f(xx), 'b');

q = polyder(p);
g = @(x)polyval(q, x);
%plot(xx, g(xx), 'y');

[ x, ~ ] = zero_bisection(g, 0, 1, 10^-5, 100);
xm1 = x;
fxm1 = f(x);
[ x, ~ ] = zero_bisection(g, 1, 2, 10^-5, 100);
xm2 = x;
fxm2 = f(x);
[ x, ~ ] = zero_bisection(g, 2.5, 4.5, 10^-5, 100);
xm3 = x;
fxm3 = f(x);
[ x, ~ ] = zero_bisection(g, 4.5, 5, 10^-5, 100);
xm4 = x;
fxm4 = f(x);

if fxm1 < fxm3
	scatter(xm1, fxm1, 'g*')
	xm1
else
	scatter(xm3, fxm3, 'g*')
	xm3
end

if fxm2 > fxm4
	scatter(xm2, fxm2, 'g*')
	xm2
else
	scatter(xm4, fxm4, 'g*')
	xm4
end
