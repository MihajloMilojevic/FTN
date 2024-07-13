x = [1 4 5];
y = [1 3 3];
scatter(x, y, 'r'), hold on
p = linterp(x, y)
xx = linspace(0, 6, 1000);
yy = polyval(p, xx);
plot(xx, yy, 'b')
plot([0 6], [2 2], 'g')
f = @(x)(polyval(p, x) - 2);

[x y] = zero_bisection(f, 0, 6, 10^-8, 100) 
plot(x, y + 2, 'k*');