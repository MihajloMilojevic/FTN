function y = zad6(A)
	[n, m] = size(A);
	x(1:n) = -inf;
	y(1:n) = 0;
	for i = 1: n
		for j = 1: m
			if A(i, j) > x(i)
				x(i) = A(i, j);
				y(i) = j;
			end
		end
	end
	return
end
