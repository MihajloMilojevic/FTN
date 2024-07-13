function A = zad8(A)
	[n m] = size(A);
	for i = 1: n
		temp = A(i, i);
		A(i, i) = A(i, n - i + 1);
		A(i, n - i + 1) = temp;
	end
	return
end