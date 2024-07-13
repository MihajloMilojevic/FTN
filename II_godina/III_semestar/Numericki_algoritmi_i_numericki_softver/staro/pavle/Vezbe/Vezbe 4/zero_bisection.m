function [ x, y ] = zero_bisection(f, a, b, errMax, plotSpeed)
	x = (a + b)/2;
	while abs(f(x)) > errMax && plotSpeed >= 0
		if f(a) >= 0 && f(b) < 0
			if f(x) > 0
				a = x; 
			else
				f(x) < 0
				b = x;
			end
		elseif f(a) <= 0 && f(b) > 0
			if f(x) > 0
				b = x; 
			else
				a = x;
			end
		end
		x = (a + b)/2;
		plotSpeed = plotSpeed - 1;
	end
	y = f(x);
	plotSpeed
	return
end

