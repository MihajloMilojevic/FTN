v = @(t) t.^2 - 2.*t + 3;
t1 = 5;
t0 = 0;
I = integrateSimpson(v, 0, 5, 100, 0)