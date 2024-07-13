function B = fz1b(A)
    rows = size(A, 1);
    centralna_kol = ceil(rows/2);
    j = 1;
    B = A;
    for i = 1:rows
        pom = B(j,centralna_kol);
        B(j, centralna_kol) = A(i,rows - i + 1);
        B(i,rows - i + 1) = pom;
        j = j + 1;
    end
end

