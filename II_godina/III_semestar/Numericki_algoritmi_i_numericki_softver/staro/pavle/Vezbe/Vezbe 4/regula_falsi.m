function [ x, y ] = regula_falsi(f, x0, x1, err, iter)
	for i=1:iter
		x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0));
		if abs(f(x2)) < err
			break;
		end
		if f(x0)*f(x2) < 0
			x1 = x2;
		else
			x0 = x1;
			x1 = x2;
		end
	end
	x = x2;
	y = f(x);
end

