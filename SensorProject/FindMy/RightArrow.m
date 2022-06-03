
senseHat.clearLEDMatrix;
% Pixel code for a right facing arrow
for i = 1:8
    writePixel(senseHat, [i 4], 'red');
end
writePixel(senseHat, [7 3], 'red');
writePixel(senseHat, [7 5], 'red');
writePixel(senseHat, [6 2], 'red');
writePixel(senseHat, [6 6], 'red');
writePixel(senseHat, [5 1], 'red');
writePixel(senseHat, [5 7], 'red');
