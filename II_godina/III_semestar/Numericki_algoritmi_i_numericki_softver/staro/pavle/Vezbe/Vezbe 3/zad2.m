x = [ 1.1960 0.2449 0.1980 ]'
y = [0.3424 1.0565 0.2631]'
z = [0.1747 0.0751 0.9159]'
b = [-2.6827 -3.7424 0.9456]'
A = [sin(x) sin(y) sin(z)]

x0 = [0 0 0]'

gaus_seidel(A, b, 1000, 10^-8, x0)