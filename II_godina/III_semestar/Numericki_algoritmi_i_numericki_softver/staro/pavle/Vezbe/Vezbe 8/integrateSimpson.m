function I = integrateSimpson(f, a, b, intervals, plotspeed)
	I = 0;
	width = (b - a)/intervals;
	x = a:width:b;
	for it = 1:2:intervals
		x1 = x(it);
		x2 = x(it+1);
		x3 = x(it+2);
		fx1 = f(x1);
		fx2 = f(x2);
		fx3 = f(x3);
		p = polyfit([x1 x2 x3], [fx1 fx2 fx3], 2);
		xp = linspace(x1, x3, 100);
		if plotspeed > 0
			area(xp, f(xp), 'FaceColor', 'blue', 'LineStyle', 'none'), hold on;
			pause(1/plotspeed);
		end
		
		I = I + (fx1 + 4*fx2 + fx3)*width/3;
	end
end

