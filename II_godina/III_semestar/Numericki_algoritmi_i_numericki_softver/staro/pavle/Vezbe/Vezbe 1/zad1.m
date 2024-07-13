function sumica = zad1(A)
    sumica = 0;
    [n, m] = size(A);
    for i = 1:n
        sumica = sumica + A(i, i);
    end
    return
end
