A = [0 1 2 
	1 2 0
	-1 -1 0]
A_changed = [1 1 2 
			1 2 0
			-1 -1 1]

b = [1 2 3]'

x0 = [0 0 0]'

gaus_seidel(A_changed, b, 1000, 10^-8, x0)

A_changed\b

U = triu(A_changed, 1)
L = tril(A_changed, -1)
D = diag(diag(A_changed))
T = -(D+L)^-1*U
ro = max(abs(eig(T)))