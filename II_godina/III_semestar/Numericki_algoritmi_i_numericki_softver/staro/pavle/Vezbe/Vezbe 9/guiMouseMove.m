function guiMouseMove(~, ~)
    mouseLocation = get(gca, 'CurrentPoint');
    setappdata(gcf, 'mouseLocation', mouseLocation)
end