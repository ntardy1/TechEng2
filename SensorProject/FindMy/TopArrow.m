
senseHat.clearLEDMatrix;
% Pixel code for an 'upwards' arrow
for i = 1:8
    writePixel(senseHat, [5 i], 'red');
end
writePixel(senseHat, [4 2], 'red');
writePixel(senseHat, [6 2], 'red');
writePixel(senseHat, [3 3], 'red');
writePixel(senseHat, [7 3], 'red');
writePixel(senseHat, [2 4], 'red');
writePixel(senseHat, [8 4], 'red');
