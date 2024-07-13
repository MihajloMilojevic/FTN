function p = linterp(x,y)
	n=length(x);
	p=0;
	for i=1:n
		L=1;
		for j=1:n 
			if i~=j
				L = conv(L,[1, -x(j)]/(x(i)-x(j)));
			end
		end
		p = p+y(i)*L;
	end
	return
end