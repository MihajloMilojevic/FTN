function fX = rk4(a, b, h, fX0, dfX, plotSpeed)
    if plotSpeed <= 0
        fX = rk4WithoutPlot(a, b, h, fX0, dfX);
        return
    end
    fX = rk4WithPlot(a, b, h, fX0, dfX, plotSpeed);
end

function fX = rk4WithoutPlot(a, b, h, fX0, dfX)
    x = a:h:b;
    n = length(x);
    
    fX = NaN(1, n);
    fX(1) = fX0;
    for it = 2:n
        k1 = dfX(x(it - 1), fX(it - 1));
        k2 = dfX(x(it - 1) + h/2, fX(it - 1) + k1*h/2);
        k3 = dfX(x(it - 1) + h/2, fX(it - 1) + k2*h/2);
        k4 = dfX(x(it - 1) + h, fX(it - 1) + k3*h);

        fX(it) = fX(it - 1) + h/6*(k1 + 2*k2 + 2*k3 + k4);
    end
end

function fX = rk4WithPlot(a, b, h, fX0, dfX, plotSpeed)
    close
    fig = figure();

    x = a:h:b;
    n = length(x);
    
    fX = NaN(1, n);
    fX(1) = fX0;
    for it = 2:n
        if ~ishandle(fig)
            return
        end

        k1 = dfX(x(it - 1), fX(it - 1));
        k2 = dfX(x(it - 1) + h/2, fX(it - 1) + k1*h/2);
        k3 = dfX(x(it - 1) + h/2, fX(it - 1) + k2*h/2);
        k4 = dfX(x(it - 1) + h, fX(it - 1) + k3*h);

        fX(it) = fX(it - 1) + h/6*(k1 + 2*k2 + 2*k3 + k4);

        plot(x, fX, 'blue', [a b], [0 0], 'black')
        pause(1/plotSpeed)
    end
end