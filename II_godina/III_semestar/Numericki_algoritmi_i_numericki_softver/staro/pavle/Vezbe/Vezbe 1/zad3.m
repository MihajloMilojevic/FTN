function x = zad3(A)
    [n, m] = size(A);
    x = zeros(m, 1);
	for i = 1: m
		mini = inf;
		for j = 1:n
			if A(j, i) < mini 
				x(i) = j;
				mini = A(j, i);
			end
		end
	end
	return
end