function x = zad5(A)
	[n, m] = size(A);
	x = [-1 -1];
	mini = inf;
	for i = 1: n
		for j = 1:m
			if j == n + 1 - i || j == i
				if A(i, j) < mini
					x = [i j];
					mini = A(i, j);
				end
			end
		end
	end
	return
end