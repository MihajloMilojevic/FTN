clc
clear all

ns0T = 0;
v0T = 0;

F = 10;
m = 1;

% s"(t) = a
% s(0) = 0, s'(0) = 0
% resenje: s(t) = v0.*t + F/m*0.5*t.^2

ddsT = @(t, s, ds) F/m;

ns0T = [ns0T v0T];

ta = 0;
tb = 10;
h = (tb - ta)/10;

t = ta:h:tb;
sTTrue = feval(@(t) v0T.*t + F/m*0.5*t.^2, t)
sTEuler = eulerN(ta, tb, h, ns0T, ddsT, 0.0)
sTRK4 = rk4N(ta, tb, h, ns0T, ddsT, 0.0)

plot(t, sTTrue, 'black', t, sTEuler, 'blue', t, sTRK4, 'red')