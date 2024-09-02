x = [1 2 3 5 6];
fX = [2 4 4 1 3];

scatter(x, fX);
hold on
p = lsquares(x, fX, 4);
f = @(x)polyval(p, x);
xx = linspace(1, 6, 100);
fxx = f(xx);
plot(xx, fxx)

xt = 4;
fxt = f(xt)
scatter(xt, fxt, 'r+')