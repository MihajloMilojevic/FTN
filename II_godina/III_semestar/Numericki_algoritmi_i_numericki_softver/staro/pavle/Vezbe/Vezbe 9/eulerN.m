function [fX, fnX] = eulerN(a, b, h, nfX0, dnfX, plotSpeed)
    if plotSpeed <= 0
        [fX, fnX] = eulerNWithoutPlot(a, b, h, nfX0, dnfX);
        return
    end
    [fX, fnX] = eulerNWithPlot(a, b, h, nfX0, dnfX, plotSpeed);
end

function [fX, fnX] = eulerNWithoutPlot(a, b, h, nfX0, dnfX)
    x = a:h:b;
    n = length(x);
    order = length(nfX0); % red diferencijalne jedna?ine

    % prva vrsta ?uva vrednosti funkcije
    % druga vrsta ?uva vrednosti 1. izvoda funkcije, itd.
    % prva kolona ?uva poznate vrednosti funkcije i njenih izvoda
    % druga kolona ?uva vrednosti funkcije i njenih izvoda u ta?ki (a + h)
    % [f(a)         f(a + h)        f(a + 2h)       ...]
    % [f'(a)        f'(a + h)       f"(a + 2h)      ...]
    % .
    % .
    % .
    % [f^(r-1)(a)	f^(r-1)(a + h)  f^(r-1)(a + 2h)	...]'
    fnX = NaN(order, n);
    fnX(:, 1) = nfX0'; 
    for it = 2:n
        % f(i) = f(i - 1) + h*f'(i - 1);
        % f'(i) = f'(i - 1) + h*f"(i - 1);
        % .
        % .
        % .
        for itOrder = 1:order - 1
            fnX(itOrder, it) = fnX(itOrder, it - 1) + h*fnX(itOrder + 1, it - 1);
        end
        % lista argumenata: [x(i - 1) f(i - 1) f'(i - 1) ... f^(r-1)(i - 1)]
        args = num2cell([x(it - 1) fnX(:, it - 1)']);
        fnX(order, it) = fnX(order, it - 1) + h*dnfX(args{:});
    end
    fX = fnX(1, :); % prva vrsta ?uva vrednosti funkcije
end

function [fX, fnX] = eulerNWithPlot(a, b, h, nfX0, dnfX, plotSpeed)
    close
    fig = figure();

    x = a:h:b;
    n = length(x);
    order = length(nfX0);

    fnX = NaN(order, n);
    fnX(:, 1) = nfX0'; 
    for it = 2:n
        if ~ishandle(fig)
            return
        end

        for itOrder = 1:order - 1
            fnX(itOrder, it) = fnX(itOrder, it - 1) + h*fnX(itOrder + 1, it - 1);
        end
        args = num2cell([x(it - 1) fnX(:, it - 1)']);
        fnX(order, it) = fnX(order, it - 1) + h*dnfX(args{:})

        plot(x, fnX(1, :), 'blue', [a b], [0 0], 'black')
        pause(1/plotSpeed)
    end
    fX = fnX(1, :);
end