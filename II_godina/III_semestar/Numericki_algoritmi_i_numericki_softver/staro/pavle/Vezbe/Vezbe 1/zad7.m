function B = zad7(A)
	[n, m] = size(A);
	B = A;
	for i = 1:2:n
		for j = 1:floor(m/2)
			temp = B(i, j);
			B(i, j) = B(i, m - j + 1);
			B(i, m - j + 1) = temp;
		end
	end
	return
end