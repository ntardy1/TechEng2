
senseHat.clearLEDMatrix;
% Pixel code for an arrow pointing to the top right corner
writePixel(senseHat, [4 5], 'red');
writePixel(senseHat, [5 4], 'red');
writePixel(senseHat, [4 5], 'red');
writePixel(senseHat, [6 3], 'red');
writePixel(senseHat, [7 2], 'red');
writePixel(senseHat, [8 1], 'red');
for i = 5:8
    writePixel(senseHat, [i 1], 'red');
end

for i = 1:4
    writePixel(senseHat, [8 i], 'red');
end
