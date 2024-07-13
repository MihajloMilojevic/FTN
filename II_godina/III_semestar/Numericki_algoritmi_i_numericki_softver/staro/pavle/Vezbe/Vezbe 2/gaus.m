function x = gaus(A, B)
	% trougaoni
	[n, ~] = size(A);
	x = zeros(n, 1);
	for i = 1:n-1
		[~, mi] = max(abs(A(i:n, i)))
		mi = i + mi - 1;
		A([i, mi], :) = A([mi, i], :)
		B([i, mi], :) = B([mi, i], :)
		for j = i+1:n
			p = -1*A(j, i)/A(i, i);
			A(j, :) = p*A(i, :) + A(j, :);
			B(j) = p*B(i) + B(j);
		end
	end
	for i = n:-1:1
		x(i) = (B(i) - A(i, i+1:n)*x(i+1:n))/A(i, i);
	end
	return
end