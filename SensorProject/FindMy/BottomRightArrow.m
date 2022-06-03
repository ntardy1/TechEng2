
senseHat.clearLEDMatrix;
% Pixel code for a bottom right facing arrow
for i = 4:8
    writePixel(senseHat, [i i], 'red');
end

for i = 5:8
    writePixel(senseHat, [i 8], 'red');
    writePixel(senseHat, [8 i], 'red');
end
