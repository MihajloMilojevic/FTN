f = @(x)(x.^2.*sin(x));
xx = linspace(-pi, pi, 1000);
yy = f(xx);
plot(xx, yy), hold on;
plot([-4 4], [0 0], 'k');
plot([0 0], [-4 4], 'k');

x = [-pi, -pi/2, pi/2, pi];
y = f(x);
p = linterp(x, y)
q = [-0.1034 0.0000 1.0203 00000]
xx = linspace(-pi, pi, 1000);
yy = polyval(p, xx);
plot(xx, yy, 'r');