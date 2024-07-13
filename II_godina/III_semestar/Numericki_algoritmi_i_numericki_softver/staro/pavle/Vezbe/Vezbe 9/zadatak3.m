clc
clear all

% f"(x) = -f(x) + x + 2
% f(0) = 4, f'(0) = 2
% rešenje: f(x) = 2cos(x) + sin(x) + x + 2

% eksplicitni oblik jedna?ine po najvisem izvodu funkcije
% zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
% izvoda, iako se ne koriste
ddfX = @(x, fX, dfX) -fX + x + 2

% PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
% za 1 manjeg od reda jedna?ine u po?etnoj ta?ki
nfX0 = [4 2];

a = 0;
b = 4*pi;
h = (b - a)/10000;

x = a:h:b;
fXTrue = feval(@(x) 2*cos(x) + sin(x) + x + 2, x);
fXEuler = eulerN(a, b, h, nfX0, ddfX, 0.0);
fXRK4 = rk4N(a, b, h, nfX0, ddfX, 0.0);

plot(x, fXTrue, 'black', x, fXEuler, 'blue', x, fXRK4, 'red')
