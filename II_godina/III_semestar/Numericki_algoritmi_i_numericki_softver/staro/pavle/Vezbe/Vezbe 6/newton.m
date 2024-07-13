function [ x, y ] = newton(f, df, x0, err, iter)
	while abs(f(x0)) > err && iter >= 0
		x0 = x0 - f(x0)/df(x0);
		iter = iter - 1
	end
	x = x0
	y = f(x)
	return
end

