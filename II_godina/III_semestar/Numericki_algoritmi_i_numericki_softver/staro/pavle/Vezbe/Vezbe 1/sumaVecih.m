function x = sumaVecih(A)
    x = 0;
    [n, m] = size(A);
    prosek = sum(A);
    prosek = sum(prosek) / (n*m);
    for i = 1:n
        for j = 1:m
            disp(A(i, j)) 
            disp(prosek)
            if A(i, j) > prosek
                x = x + A(i, j);
            end
        end
    end
    return
end
