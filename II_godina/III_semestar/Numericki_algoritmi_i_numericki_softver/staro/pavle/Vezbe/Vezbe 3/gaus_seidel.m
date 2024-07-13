function x = gaus_seidel(A, b, maxIter, tol, x0)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
	xk = x0;
	xk1 = x0;
	[n m] = size(A);
	for k = 1: maxIter
		for i = 1:n
			s = 0;
			for j = 1:i-1
				s = s + A(i, j)*xk1(j);
			end
			for j = i+1:n
				s = s + A(i, j)*xk(j);
			end
			xk1(i) = (b(i) - s)/A(i, i);
		end
		if(abs(xk - xk1) < tol)
			break;
		end
		xk = xk1;
	end
	x = xk1;
	return

end

