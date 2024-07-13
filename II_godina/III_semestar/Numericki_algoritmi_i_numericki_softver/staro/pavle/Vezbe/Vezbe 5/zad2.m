x = [1, 2, 4];
y = [4, 5, 4];

scatter(x, y, 'r*'), hold on
p = linterp(x, y);
xx = linspace(0, 5, 1000);
yy = polyval(p, xx);
plot(xx, yy, 'b');
scatter(3, polyval(p, 3), 'g*')
