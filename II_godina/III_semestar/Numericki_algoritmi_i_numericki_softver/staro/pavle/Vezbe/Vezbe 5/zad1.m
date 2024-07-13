x = [0.7854, 1.9635, 3.1416, 4.3198, 5.4978];
y = [0.7071, 0.9239, 0.0000, -0.9239, -0.7071];
p = linterp(x, y)
polyval(p, 0.7854)
plot([0 10], [0 0], 'k')
hold on;
scatter(x, y, 'r*');
xx = linspace(0, 6, 1000);
yy = polyval(p, xx);
plot(xx, yy, 'b');