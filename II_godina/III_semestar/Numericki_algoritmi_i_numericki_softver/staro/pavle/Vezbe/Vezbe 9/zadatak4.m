clc
clear all

% f(x)"" = -13f"(x) - 36f(x)
% f(0) = 0, f'(0) = -3, f"(0) = 5, f"'(0) = -3
% rešenje: f(x) = cos(2x) - 3sin(2x) - cos(3x) + sin(3x)

% eksplicitni oblik jedna?ine po najvisem izvodu funkcije
% zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
% izvoda, iako se ne koriste
ddddfX = @(x, fX, dfX, ddfX, dddfX) -13*ddfX - 36*fX

% PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
% za 1 manjeg od reda jedna?ine u po?etnoj ta?ki
nfX0 = [0 -3 5 -3];

a = 0;
b = 4*pi;
h = (b - a)/10000;

x = a:h:b;
fXTrue = feval(@(x) cos(2*x) - 3*sin(2*x) - cos(3*x) + sin(3*x), x);
fXEuler = eulerN(a, b, h, nfX0, ddddfX, 0.0);
fXRK4 = rk4N(a, b, h, nfX0, ddddfX, 0.0);

plot(x, fXTrue, 'black', x, fXEuler, 'blue', x, fXRK4, 'red')
