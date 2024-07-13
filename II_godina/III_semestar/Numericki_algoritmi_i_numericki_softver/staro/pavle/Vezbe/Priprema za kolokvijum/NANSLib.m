classdef NANSLib    
    %NANSLib Biblioteka funkcija koje se koriste na predmetu NANS
    %   Klasa NANSLib sadrzi staticke metode koje su implementirane na vezbama 
    %   Dostupne metode:
    %       <a href="matlab:help NANSLib.gauss_PP">gauss_PP(...)</a> 
    %       <a href="matlab:help NANSLib.gs">gs(...)</a>
    %       <a href="matlab:help NANSLib.zeroBisection">zeroBisection(...)</a>
    %       <a href="matlab:help NANSLib.zeroFalsePosition">zeroFalsePosition(...)</a>
    %       <a href="matlab:help NANSLib.zeroSecant">zeroSecant(...)</a>
    %       <a href="matlab:help NANSLib.zeroNewton">zeroNewton(...)</a>
    %       <a href="matlab:help NANSLib.lagrangeInterp">lagrangeInterp(...)</a>
    %       <a href="matlab:help NANSLib.lSquares">lSquares(...)</a>
    methods (Static)
        function x = gauss_PP(A, b)
            % Metoda Gauss-a sa parcijalnim pivotingom za resavanje SLAJ
            %   Pozivanje:
            %       x = NANSLib.gauss_PP(A, b)
            %   Parametri:
            %       A - matrica koeficijenata nepoznatih sistema jednacina, dimenzije NxN
            %       b - vektor slobodnih koeficijenata sistema jednacina, dimenzije Nx1
            %   Povratne vrednosti:
            %       x - vektor resenja sistema jednacina, dimenzije Nx1
            [rows, cols] = size(A);
            if rows ~= cols
                error('Matrix A must be square!')
            end

            [A, b] = upperTriangular_PP(A, b);
            x = solveUpperTriangular(A, b);
            
            function [A, b] = upperTriangular_PP(A, b)
                rows = size(A, 1);
                for it1 = 1:rows - 1
                    [~, mi] = max(abs(A(it1:rows, it1)));
                    mi = mi + it1 - 1;
                    A([it1,mi],:) = A([mi,it1],:);
                    b([it1,mi]) = b([mi,it1]);
                    for it2 = it1 + 1:rows
                        m = A(it2,it1)/A(it1,it1);
                        A(it2,:) = A(it2,:) - A(it1,:)*m;
                        b(it2) = b(it2) - b(it1)*m;
                    end
                end
            end

            function x = solveUpperTriangular(A, b)
                rows = size(A, 1);
                x = zeros(rows, 1);
                for it1 = rows:-1:1
                    x(it1) = (b(it1) - A(it1,it1 + 1:end)*x(it1 + 1:end))/A(it1,it1);
                end
            end
        end
        function [x, it] = gs(A, b, x0, itMax, errMax)
            % Metoda Gauss-Seidel za resavanje SLAJ iterativnim putem
            %   Pozivanje:
            %       [x, it] = NANSLib.gs(A, b, x0, itMax, errMax)
            %   Parametri:
            %       A - matrica koeficijenata nepoznatih sistema jednacina, dimenzije NxN
            %       b - vektor slobodnih koeficijenata sistema jednacina, dimenzije Nx1
            %       x0 - vektor pocetnih resenja sistema jednacina, dimenzije Nx1
            %       itMax - maksimalan broj iteracija u slucaju divergencije
            %       errMax - vrednost maksimalne greske 
            %           tj. trazene preciznosti resenja u slucaju konvergencije
            %   Povratne vrednosti:
            %       x - vektor resenja sistema jednacina, dimenzije Nx1
            %       it - broj iteracije u kojoj je metoda konvergirala/divergirala 
            [rows, cols] = size(A);
            if(rows ~= cols)
                error('Matrix A must be square!')
            end

            x = x0;
            for it = 1:itMax
                for row = 1:rows
                    x(row) = 1/A(row,row)*(b(row) - A(row,1:row - 1)*x(1:row - 1) - A(row,row + 1:end)*x0(row + 1:end));
                end
                if abs(x - x0) < errMax
                    return
                end
                x0 = x;
            end
        end
        function [zero, it] = zeroBisection(f, a, b, errMax)
            % Metoda polovljenja za trazenje nule funkcije
            %   Pozivanje:
            %       [zero, it] = NANSLib.zeroBisection(f, a, b, errMax)
            %   Parametri:
            %       f - funkcija
            %       a - vrednost pocetka intervala
            %       b - vrednost kraja intervala
            %       errMax - vrednost maksimalne greske 
            %           tj. trazene preciznosti resenja u slucaju konvergencije
            %   Povratne vrednosti:
            %       zero - X vrednost nule funkcije f
            %       it - vrednost iteracije u kojoj je metoda konvergirala 
            if f(a)*f(b) > 0
                error('f(a)*f(b) > 0!')
            end

            [zero, it] = zeroBisectionWithoutPlot(f, a, b, errMax);
            
            function [zero, it] = zeroBisectionWithoutPlot(f, a, b, errMax)
                it = 1;
                while true
                    zero = (a + b)/2;

                    fZero = f(zero);
                    if abs(fZero) < errMax || abs(b - a) < errMax
                        return
                    end

                    if f(a)*fZero < 0
                        b = zero;
                    else
                        a = zero;
                    end
                    it = it + 1;
                end
            end
        end
        function [zero, it] = zeroFalsePosition(f, a, b, errMax)
            % Metoda regula falsi za pronalazenje nule funkcije
            %   Pozivanje:
            %       [zero, it] = NANSLib.zeroFalsePosition(f, a, b, errMax)
            %   Parametri:
            %       f - funkcija
            %       a - vrednost pocetka intervala
            %       b - vrednost kraja intervala
            %       errMax - vrednost maksimalne greske 
            %           tj. trazene preciznosti resenja u slucaju konvergencije
            %   Povratne vrednosti:
            %       zero - X vrednost nule funkcije f
            %       it - vrednost iteracije u kojoj je metoda konvergirala
            if f(a)*f(b) > 0
                error('f(a)*f(b) > 0!')
            end

            [zero, it] = zeroFalsePositionWithoutPlot(f, a, b, errMax);
            
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
        end
        function [zero, it] = zeroSecant(f, a, b, errMax, itMax)
            % Metoda secice za pronalazenje nule funkcije
            %   Pozivanje:
            %       [zero, it] = NANSLib.zeroSecant(f, a, b, errMax, itMax)
            %   Parametri:
            %       f - funkcija
            %       a - vrednost pocetka intervala
            %       b - vrednost kraja intervala
            %       errMax - vrednost maksimalne greske 
            %           tj. trazene preciznosti resenja u slucaju konvergencije
            %       itMax - maksimalan broj iteracija u slucaju divergencije
            %   Povratne vrednosti:
            %       zero - X vrednost nule funkcije f
            %       it - vrednost iteracije u kojoj je metoda konvergirala/divergira
            if f(a) == f(b)
                error('f(a) == f(b)!')
            end

            [zero, it] = zeroSecantWithoutPlot(f, a, b, errMax, itMax);
            
            function [zero, it] = zeroSecantWithoutPlot(f, a, b, errMax, itMax)
                for it = 1:itMax
                    fA = f(a);
                    fB = f(b);
                    zero = b - fB*(b - a)/(fB - fA);

                    fZero = f(zero);
                    if abs(fZero) < errMax
                        return
                    end

                    a = b;
                    b = zero;
                end
            end
        end
        
        function [zero, it] = zeroNewton(f, df, x0, errMax, itMax)
            % Newton-ova metoda (tangente) za pronalazenje nule funkcije
            %   Pozivanje:
            %       [zero, it] = NANSLib.zeroNewton(f, df, x0, errMax, itMax)
            %   Parametri:
            %       f - funkcija
            %       df - izvod funkcije f
            %       x0 - vrednost pocetka intervala 
            %       errMax - vrednost maksimalne greske 
            %           tj. trazene preciznosti resenja u slucaju konvergencije
            %       itMax - maksimalan broj iteracija u slucaju divergencije
            %   Povratne vrednosti:
            %       zero - X vrednost nule funkcije f
            %       it - vrednost iteracije u kojoj je metoda konvergirala/divergira
            if df(x0) == 0
                error('df(x0) == 0!')
            end

            [zero, it] = zeroNewtonWithoutPlot(f, df, x0, errMax, itMax);
            
            function [zero, it] = zeroNewtonWithoutPlot(f, df, x0, errMax, itMax)
                for it = 1:itMax
                    zero = x0 - f(x0)/df(x0);

                    fZero = f(zero);
                    if abs(fZero) < errMax
                        return
                    end
                    x0 = zero;
                end
            end
        end
        
        function p = lagrangeInterp(x, fX)
            % Metoda Lagrange-ove interpolacije skupa tacaka polinomom
            %   Pozivanje:
            %       p = NANSLib.lagrangeInterp(x, fX)
            %   Parametri:
            %       x - vektor X vrednosti tacaka, dimenzije 1xN
            %       fX - vektor Y vrednosti tacaka, dimenzije 1xN
            %   Povratne vrednosti:
            %       p - vektor koeficijenata interpolacionog polinoma
            order = length(x) - 1;

            p = 0;
            for itFX = 1:order + 1
                lNumer = 1;
                lDenom = 1;
                for itX = 1:itFX - 1
                    lNumer = conv(lNumer, [1 -x(itX)]);
                    lDenom = lDenom*(x(itFX) - x(itX));
                end
                for itX = itFX + 1:order + 1
                    lNumer = conv(lNumer, [1 -x(itX)]);
                    lDenom = lDenom*(x(itFX) - x(itX));          
                end
                p = p + lNumer/lDenom*fX(itFX);
            end
        end
        
        function p = lSquares(x, fX, order)
            % Metoda najmanjih kvadrata za aproksimaciju funkcija polinomom
            %   Pozivanje:
            %       p = NANSLib.lSquares(x, fX, order)
            %   Parametri:
            %       x - vektor X vrednosti tacaka, dimenzije 1xN
            %       fX - vektor Y vrednosti tacaka, dimenzije 1xN
            %       order - stepen aproksimacionog polinoma
            %   Povratne vrednosti:
            %       p - vektor koeficijenata interpolacionog polinoma
            n = length(x);
            m = min(order + 1, n);

            x = x';
            fX = fX';

            A = zeros(n, m);
            for it = 1:m
                A(:, it) = x.^(it - 1);
            end
            a = (A'*A)\(A'*fX);
            p = fliplr(a');
        end
    end
    
end

