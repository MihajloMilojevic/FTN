function s = fz1a(A, br)
    b = unique(A);
    [rows, cols] = size(A);
    s = 0;
    for row = 1:length(b)
       count = 0;
       for col = 1:rows
           for k = 1:cols
               if A(col,k) == b(row)
                   count = count + 1;
               end
           end
       end
       if count >= br
           s = s + b(row);
       end
    end
end
