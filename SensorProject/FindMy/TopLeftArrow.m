
senseHat.clearLEDMatrix;
% Pixel code for top left facing arrow

for i = 1:5
    writePixel(senseHat, [i i], 'red');
end

for i = 1:4
    writePixel(senseHat, [i 1], 'red');
    writePixel(senseHat, [1 i], 'red');
end
