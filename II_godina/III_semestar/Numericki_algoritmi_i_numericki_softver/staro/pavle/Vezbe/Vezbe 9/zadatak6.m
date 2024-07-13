clc
clear all;

dhT = @(t, hT) -sin(2*t) + 0.2*hT;

% a)
hT0 = 2;

t0 = 5.5;
tb = 10;
step = (tb - t0)/1000;

vRK4 = rk4N(t0, tb, step, hT0, dhT, 0.0);

r = 3;

v1 = r.^2*pi*hT0;
v2 = r.^2*pi*vRK4(length(vRK4));
dv = v2 - v1 % zapremina ulivene vode je jednaka razlici zapremina u krajevima intervala

% b)
hT0 = 8;

t0 = 2;
tb = 10; % pretpostavljeni dovoljno dug interval
step = (tb - t0)/1000;

hTRK4 = rk4N(t0, tb, step, hT0, dhT, 0.0);

% aproksimacija funkcije radi nalaženja ta?ke za datu vrednost
% proizvoljan dovoljno dobar stepen polinoma
x = t0:step:tb;
p = lSquares(x, hTRK4, 7);

a = 2;
b = 10;

x = linspace(a, b, 100);
hT1 = 16;

plot(x, polyval(p, x), [a, b], [hT1, hT1]), hold on

t1 = zeroFalsePosition(@(x) polyval(p, x) - hT1, a, b, 10^-5, 0.0)
scatter(t1, hT1), hold off
