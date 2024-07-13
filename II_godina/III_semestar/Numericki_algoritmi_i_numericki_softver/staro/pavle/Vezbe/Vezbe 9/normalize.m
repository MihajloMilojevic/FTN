function out = normalize(in)
    magnitude = norm(in);
    if magnitude == Inf || magnitude <= 0
        out = [1, 0];
    else
        out = in/magnitude;
    end
end

