clc
clear all

% f"(x) = -sin(x)
% f(0) = 0, f'(0) = 1
% rešenje: f(x) = sin(x)

% eksplicitni oblik jedna?ine po najvišem izvodu funkcije
% zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
% izvoda, iako se ne koriste
ddfX = @(x, fX, dfX) -sin(x)

% PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
% za 1 manjeg od reda jedna?ine u po?etnoj ta?ki
nfX0 = [0 1];

a = 0;
b = 4*pi;
h = (b - a)/10000;

x = a:h:b;
fXTrue = feval(@(x) sin(x), x);
fXEuler = eulerN(a, b, h, nfX0, ddfX, 0.0);
fXRK4 = rk4N(a, b, h, nfX0, ddfX, 0.0);

plot(x, fXTrue, 'black', x, fXEuler, 'blue', x, fXRK4, 'red')