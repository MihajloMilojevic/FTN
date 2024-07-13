x = [1 3 5];
y = [0 3 0];
scatter(x, y, 'r*'), hold on;

p = linterp(x, y)
xx = linspace(0, 6, 1000);
yy = polyval(p, xx);
plot(xx, yy, 'b');
plot([0 6], [1 1], 'g')
f = @(x)(polyval(p, x)-1)
[x y] = zero_bisection(f, 0, 3, 10^-8, 100)
scatter(x, 1, 'k*')
[x y] = zero_bisection(f, 3, 6, 10^-8, 100)
scatter(x, 1, 'k*')
