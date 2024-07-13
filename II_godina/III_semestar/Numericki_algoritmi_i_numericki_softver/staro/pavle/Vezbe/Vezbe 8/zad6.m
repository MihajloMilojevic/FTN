f = @(x) x.^2 + 2;
g = @(x) sqrt(x - 2);
I1 = integrateSimpson(g, 2, 4, 100, 0)