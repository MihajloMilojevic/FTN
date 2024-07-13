clc
clear all

f = @(x) exp(x)/2.*cos(x.^2/3);
x = linspace(1, 6, 100);
plot(x,f(x)), hold on

%a) aproksimirati polinomom 7. stepena
xx = linspace(1,6,8);
p = NANSLib.lagrangeInterp(xx,f(xx))
pol = @(x) polyval(p,x);
plot(x, pol(x))

%b) naci tacke u kojoj polinom ima vrednost 35 u intervalu [4.5,6]
plot([4.5 6], [35 35], 'black')
h = @(x) polyval(p, x) - 35;
[zero1, it1] = NANSLib.zeroFalsePosition(h, 4.5, 5, 10^-5)
[zero2, it2] = NANSLib.zeroFalsePosition(h, 5.5, 6, 10^-5)
scatter(zero1, polyval(p, zero1), 'black')
scatter(zero2, polyval(p, zero2), 'black')

%c) presecne tacke funkcije i polinoma [4.5,5.5]
t = @(x) polyval(p,x) - f(x);
[zero_presek1, it_presek1] = NANSLib.zeroFalsePosition(t, 4.5, 5, 10^-5)
[zero_presek2, it_presek2] = NANSLib.zeroFalsePosition(t, 5, 5.5, 10^-5)
scatter(zero_presek1, polyval(p, zero_presek1), 'red')
scatter(zero_presek2, polyval(p, zero_presek2), 'red'), hold off

