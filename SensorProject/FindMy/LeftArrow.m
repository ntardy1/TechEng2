
senseHat.clearLEDMatrix;
% Pixel code for left arrow

for i = 1:8
    writePixel(senseHat, [i 4], 'red');
end

writePixel(senseHat, [2 3], 'red');
writePixel(senseHat, [2 5], 'red');
writePixel(senseHat, [3 2], 'red');
writePixel(senseHat, [3 6], 'red');
writePixel(senseHat, [4 1], 'red');
writePixel(senseHat, [4 7], 'red');
