function I = integrateTrapezoid(f, a, b, intervals, plotspeed)
	I = 0;
	width = (b - a)/intervals;
	x = a:width:b;
	for it=1:intervals
		x1 = x(it);
		x2 = x(it + 1);
		fx1 = f(x1);
		fx2 = f(x2);
		I = I + (fx1 + fx2)*width/2
		if plotspeed > 0
			area([x1 x2], [fx1 fx2], 'FaceColor', 'blue', 'LineStyle',	'none');
			pause(1/plotspeed);
		end
	end

end
