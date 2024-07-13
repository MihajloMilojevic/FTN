function [zero, it] = zeroFalsePosition(f, a, b, errMax, plotSpeed)
    if f(a)*f(b) > 0
        error('f(a)*f(b) > 0!')
    end

    if plotSpeed <= 0
        [zero, it] = zeroFalsePositionWithoutPlot(f, a, b, errMax);
        return
    end
    [zero, it] = zeroFalsePositionWithPlot(f, a, b, errMax, plotSpeed);
end

function [zero, it] = zeroFalsePositionWithoutPlot(f, a, b, errMax)
    it = 1;
    while true
        fA = f(a);
        fB = f(b);
        zero = b - fB*(b - a)/(fB - fA);

        fZero = f(zero);
        if abs(fZero) < errMax || abs(fZero) < errMax
            return
        end

        if fA*fZero < 0
            b = zero;
        else
            a = zero;
        end
        it = it + 1;
    end
end

function [zero, it] = zeroFalsePositionWithPlot(f, a, b, errMax, plotSpeed)
    close
    fig = figure();
   
    x = linspace(a, b, 100);
    fX = f(x);
    fMin = min(fX);
    fMax = max(fX);
    plot(x, fX, 'blue', [a b], [0 0], 'black'), hold on

    it = 1;
    while ishandle(fig)
        fA = f(a);
        fB = f(b);
        zero = b - fB*(b - a)/(fB - fA);
        plot([a b], [fA fB], 'red', zero, 0, 'x red')

        fZero = f(zero);
        plot([zero zero], [fMin, fMax], 'green', zero, fZero, 'o green')
        if abs(fZero) < errMax || abs(fZero) < errMax
            return
        end
        pause(1/plotSpeed)

        if fA*fZero < 0
            b = zero;
        else
            a = zero;
        end
        it = it + 1;
        
        plot([zero zero], [fMin, fMax], 'red', zero, fZero, 'o red')
    end
end