
senseHat.clearLEDMatrix;
% Pixel code for bottom left arrow

writePixel(senseHat, [1 8], 'red');
writePixel(senseHat, [2 7], 'red');
writePixel(senseHat, [3 6], 'red');
writePixel(senseHat, [4 5], 'red');
writePixel(senseHat, [5 4], 'red');

for i = 5:8
    writePixel(senseHat, [1 i], 'red');
end

for i = 1:4
    writePixel(senseHat, [i 8], 'red');
end
