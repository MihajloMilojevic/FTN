function [fX, fnX] = rk4N(a, b, h, nfX0, dnfX, plotSpeed)
    if plotSpeed <= 0
        [fX, fnX] = rk4NWithoutPlot(a, b, h, nfX0, dnfX);
        return
    end
    [fX, fnX] = rk4NWithPlot(a, b, h, nfX0, dnfX, plotSpeed);
end

function [fX, fnX] = rk4NWithoutPlot(a, b, h, nfX0, dnfX)
    x = a:h:b;
    n = length(x);
    order = length(nfX0);

    fnX = NaN(order, n);
    fnX(:, 1) = nfX0';

    k1 = NaN(1, order);
    k2 = NaN(1, order);
    k3 = NaN(1, order);
    k4 = NaN(1, order);
    for it = 2:n
        for itOrder = 1:order - 1
            k1(itOrder) = fnX(itOrder + 1, it - 1);
        end
        args = num2cell([x(it - 1) fnX(:, it - 1)']);
        k1(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k2(itOrder) = fnX(itOrder + 1, it - 1) + h/2*k1(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h/2 fnX(:, it - 1)' + h/2*k1]);
        k2(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k3(itOrder) = fnX(itOrder + 1, it - 1) + h/2*k2(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h/2 fnX(:, it - 1)' + h/2*k2]);
        k3(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k4(itOrder) = fnX(itOrder + 1, it - 1) + h*k3(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h fnX(:, it - 1)' + h*k3]);
        k4(order) = dnfX(args{:});

        for itOrder = 1:order
            fnX(itOrder, it) = fnX(itOrder, it - 1) + h/6*(k1(itOrder) + 2*k2(itOrder) + 2*k3(itOrder) + k4(itOrder));
        end
    end
    fX = fnX(1, :);
end

function [fX, fnX] = rk4NWithPlot(a, b, h, nfX0, dnfX, plotSpeed)
    close
    fig = figure();

    x = a:h:b;
    n = length(x);
    order = length(nfX0);

    fnX = NaN(order, n);
    fnX(:, 1) = nfX0';

    k1 = NaN(1, order);
    k2 = NaN(1, order);
    k3 = NaN(1, order);
    k4 = NaN(1, order);
    for it = 2:n
        if ~ishandle(fig)
            return
        end

        for itOrder = 1:order - 1
            k1(itOrder) = fnX(itOrder + 1, it - 1);
        end
        args = num2cell([x(it - 1) fnX(:, it - 1)']);
        k1(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k2(itOrder) = fnX(itOrder + 1, it - 1) + h/2*k1(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h/2 fnX(:, it - 1)' + h/2*k1]);
        k2(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k3(itOrder) = fnX(itOrder + 1, it - 1) + h/2*k2(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h/2 fnX(:, it - 1)' + h/2*k2]);
        k3(order) = dnfX(args{:});

        for itOrder = 1:order - 1
            k4(itOrder) = fnX(itOrder + 1, it - 1) + h*k3(itOrder + 1);
        end
        args = num2cell([x(it - 1) + h fnX(:, it - 1)' + h*k3]);
        k4(order) = dnfX(args{:});

        for itOrder = 1:order
            fnX(itOrder, it) = fnX(itOrder, it - 1) + h/6*(k1(itOrder) + 2*k2(itOrder) + 2*k3(itOrder) + k4(itOrder));
        end

        plot(x, fnX(1, :), 'blue', [a b], [0 0], 'black')
        pause(1/plotSpeed)
    end
    fX = fnX(1, :);
end