function x = zad4(A)
	[n, m] = size(A);
	x = zeros(n, 1);
	for i = 1: n
		for j = 1: m
			if j ~= n-i+1
				x(i) = x(i) + A(i, j);
			end
		end
	end
	return
end