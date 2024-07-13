clc
clear all

sT0 = 0;
vT0 = 0;
sT0 = [sT0, vT0];

t0 = 0;
t1 = 60*20;
h = (t1 - t0)/10000;

sRK4 = rk4N(t0, t1, h, sT0, @fp2, 0.0);

x = t0:h:t1;
plot(x, sRK4)

sT1 = sRK4(end)