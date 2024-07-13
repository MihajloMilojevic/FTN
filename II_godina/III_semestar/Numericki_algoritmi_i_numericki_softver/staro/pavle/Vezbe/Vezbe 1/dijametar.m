function x = dijametar(A)
	[n, m] = size(A)
	maxi = -inf
	for i = 1: n - 1
		for j = i+1:n
			x1 = A(i, 1);
			y1 = A(i, 2);
			x2 = A(j, 1);
			y2 = A(j, 2);
			d = sqrt((x2 - x1)^2 +(y2 - y1)^2)
			if d > maxi
				maxi = d
			end
		end
	end
	x = maxi
	return
end