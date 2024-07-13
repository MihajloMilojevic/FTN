clc
clear all

%a)
f = @(x) x.*cos(2*x) - 2;
a = -3*pi/2;
b = 3*pi/4;
x = linspace(a,b,100);
plot(x,f(x), 'blue'), hold on
plot([a b], [0 0], 'black')

%zeroBisection) - pronaci nulu
[zero, it] = NANSLib.zeroSecant(f, -4.5, -3.5, 10^-5, 100)
scatter(zero, f(zero), 'red')
%[zero, it] = NANSLib.zeroSecant(f, a, b, 10^-5, 100) - pogresno

%c) pronalazenje min i max
%videti koji je izvod uz pomocu df = matlabFunction(diff(sym(f)))
df = @(x)cos(x.*2.0)-x.*sin(x.*2.0).*2.0
%[zero, it] = NANSLib.zeroSecant(df, a, -1, 10^-5, 100) - neispravno,
%nadje lokalno
%[zero, it] = NANSLib.zeroSecant(df, a, b, 10^-5, 100) - neispravno,
%nadje van intervala
[minimum, it_min] = NANSLib.zeroSecant(df, -4, -2.5, 10^-5, 100)
[maximum, it_max] = NANSLib.zeroSecant(df, -5, -4.5, 10^-5, 100)
scatter(minimum, f(minimum), 'black')
scatter(maximum, f(maximum), 'black')

%d) pronalazenje preseka sa f-jom g(x)
g = @(x) -sin(x).*exp(x) - 2;
plot(x, g(x), 'green')
h = @(x) x.*cos(2*x) - 2 + sin(x).*exp(x) + 2;
%[zero_presek, it_presek] = NANSLib.zeroSecant(h, a, b, 10^-5, 100) -
%pogresno
%[zero_presek, it_presek] = NANSLib.zeroBisection(h, a, b, 10^-5) - pogresno
%[zero_presek, it_presek] = NANSLib.zeroFalsePosition(h, a, b, 10^-5) -
%pogresno
[presek1, it_presek1] = NANSLib.zeroSecant(h, -4.5, -3.5, 10^-5, 100)
[presek2, it_presek2] = NANSLib.zeroSecant(h, -2.8, -2, 10^-5, 100)
[presek3, it_presek3] = NANSLib.zeroSecant(h, -1.5, -0.5, 10^-5, 100)
[presek4, it_presek4] = NANSLib.zeroSecant(h, -0.5, 0.5, 10^-5, 100)

scatter(presek1, f(presek1), 'red')
scatter(presek2, f(presek2), 'red')
scatter(presek3, f(presek3), 'red')
scatter(presek4, f(presek4), 'red'), hold off


