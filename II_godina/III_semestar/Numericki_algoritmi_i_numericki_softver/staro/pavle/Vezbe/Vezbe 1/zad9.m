function B = zad9(A)
	[n, m] = size(A);
	B = A;
	for i = 1:2:m
		for j = 1:floor(n/2)
			temp = B(j, i);
			B(j, i) = B(n - j + 1, i);
			B(n - j + 1, i) = temp;
		end
	end
	return
end