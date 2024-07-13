function A = sortByFirstColumn(A)
	[n, m] = size(A);
	for i = 1:n-1;
		for j = i + 1: n
			if A(i, 1) < A(j, 1)
				temp = A(i, :);
				A(i, :) = A(j, :);
				A(j, :) = temp;
			end
		end
	end
	return
end