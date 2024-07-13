function x = stocksShare(years, total)
	p = sum(years);
	k = total / p;
	[n, m] = size(years);
	x = zeros(m, 1);
	for i = 1:m
		x(i) = round(years(i) * k);
	end
	return
end