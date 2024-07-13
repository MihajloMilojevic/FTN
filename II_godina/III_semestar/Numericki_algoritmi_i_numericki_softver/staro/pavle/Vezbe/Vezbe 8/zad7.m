f = @(x) x.^2 + 2;
g1 = @(x) sqrt(x - 2);
g2 = @(x) -1*sqrt(x - 2);
j = @(x) 16;
h1 = @(x) g1(x) .^ 2;
h2 = @(x) g2(x) .^ 2;

I1 = pi*integrateSimpson(h1, 2, 18, 100, 0)
I2 = pi*integrateSimpson(j, 0, 2, 100, 0)
I3 = pi*integrateSimpson(j, 2, 18, 100, 0)
I3 - I1 + I2

