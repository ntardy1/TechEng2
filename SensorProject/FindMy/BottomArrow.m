
senseHat.clearLEDMatrix;
% Pixel code for bottom facing arrow

for i = 1:8
    writePixel(senseHat, [5 i], 'red');
end

writePixel(senseHat, [5 8], 'red');
writePixel(senseHat, [4 7], 'red');
writePixel(senseHat, [6 7], 'red');
writePixel(senseHat, [3 6], 'red');
writePixel(senseHat, [7 6], 'red');
writePixel(senseHat, [8 5], 'red');
writePixel(senseHat, [2 5], 'red');
