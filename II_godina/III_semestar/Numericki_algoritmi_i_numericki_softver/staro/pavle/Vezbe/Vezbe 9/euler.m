function fX = euler(a, b, h, fX0, dfX, plotSpeed)
    if plotSpeed <= 0
        fX = eulerWithoutPlot(a, b, h, fX0, dfX);
        return
    end
    fX = eulerWithPlot(a, b, h, fX0, dfX, plotSpeed);
end

function fX = eulerWithoutPlot(a, b, h, fX0, dfX)
    x = a:h:b;
    n = length(x);

    fX = NaN(1, n);
    fX(1) = fX0;
    for it = 2:n
        fX(it) = fX(it - 1) + h*dfX(x(it - 1), fX(it - 1));
    end
end

function fX = eulerWithPlot(a, b, h, fX0, dfX, plotSpeed)
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

        fX(it) = fX(it - 1) + h*dfX(x(it - 1), fX(it - 1))

        plot(x, fX, 'blue', [a b], [0 0], 'black')
        pause(1/plotSpeed)
    end
end

