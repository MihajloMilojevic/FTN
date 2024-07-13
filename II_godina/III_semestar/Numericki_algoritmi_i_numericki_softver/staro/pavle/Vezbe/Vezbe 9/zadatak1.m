clc
clear all;

% f(x)' = cos(x)
% f(0) = 0
% rešenje: f(x) = sin(x)

% eksplicitni oblik jedna?ine po najvišem izvodu funkcije
% zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
% izvoda, iako se ne koriste
dfX = @(x, fX) cos(x)

% PPV mora da ima definisanu vrednost funkcije u po?etnoj ta?ki
fX0 = 0;

a = 0;
b = 2*pi;
h = (b - a)/10000;

x = a:h:b;
fXTrue = feval(@(x) sin(x), x);
fXEuler = eulerN(a, b, h, fX0, dfX, 0.0);
fXRK4 = rk4N(a, b, h, fX0, dfX, 0.0);

plot(x, fXTrue, 'black', x, fXEuler, 'blue', x, fXRK4, 'red')