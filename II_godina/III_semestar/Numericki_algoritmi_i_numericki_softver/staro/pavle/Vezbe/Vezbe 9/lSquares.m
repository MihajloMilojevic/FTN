function p = lSquares(x, fX, order)
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

