function [ x, y ] = secica(f, x0, x1, err, iter)
%UNTITLED9 Summary of this function goes here
%   Detailed explanation goes here
	x = x0 + (f(x1) - f(x0))/((x0 - x1)*f(x0))
	while abs(f(x)) > err && iter >= 0
		x = x0 + (x0 - x1)/((f(x1) - f(x0)))*f(x0)
		x0 = x
		iter = iter - 1
	end
	y = f(x)
	return
end

