
% Run these commands to set up the necessary systems
%{
m = mobiledev
mypi = raspi
senseHat = sensehat(mypi)
%}

%{
Meters to Degrees:
6 decimals - within about 1 meter
7 decimals - centimeter accuracy
%}

clc;

% Resetting the LED matrix
senseHat.clearLEDMatrix;

% Starting Latitude for the RPi, dependent on the user
startingLatitude = 0;
% Starting Longitude for the RPi, dependent on the user
startingLongitude = 0;

% Establishing intial GPS coordinates and getting senseHat readings
piLatitude = startingLatitude;
piLongitude = startingLongitude;
joyStick = readJoystick(senseHat);
acceleration = readAcceleration(senseHat);
YVelocity = 0;
XVelocity = 0;
YPosition = 0;
XPosition = 0;

disp("Point the RPi such that the GPIO pins are facing North");

% Logics that set up the intial orientiation for the RPi (facing North)
while true
    joyStick = readJoystick(senseHat);
    if (joyStick == 1)
        break;
    end
end

% Code should stop when RPi is within about 1m of the phone, but it updates
% the RPi's location by the centimeter
while all(abs(piLatitude - vpa(m.Latitude, 7)) > 0.00001) || all(abs(piLongitude - vpa(m.Longitude, 7)) > 0.00001)
    pause(0.5);
    if all(abs(piLatitude - m.Latitude) > 0.00001) && all(piLatitude - m.Latitude < 0) && all(abs(piLongitude - m.Longitude) < 0.00001)
        TopArrow;
    elseif all(abs(piLatitude - m.Latitude) > 0.00001) && (piLatitude - m.Latitude) > 0 && all(abs(piLongitude - m.Longitude) < 0.00001)
        BottomArrow;
    elseif all(abs(piLatitude - m.Latitude) < 0.00001) && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) > 0
        LeftArrow;
    elseif all(abs(piLatitude - m.Latitude) < 0.00001) && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) < 0
        RightArrow;
    elseif all(abs(piLatitude - m.Latitude) > 0.00001) && (piLatitude - m.Latitude) < 0 && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) > 0
        TopLeftArrow;
    elseif all(abs(piLatitude - m.Latitude) > 0.00001) && (piLatitude - m.Latitude) < 0 && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) < 0
        TopRightArrow;
    elseif all(abs(piLatitude - m.Latitude) > 0.00001) && (piLatitude - m.Latitude) > 0 && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) > 0
        BottomLeftArrow;
    elseif all(abs(piLatitude - m.Latitude) > 0.00001) && (piLatitude - m.Latitude) > 0 && all(abs(piLongitude - m.Longitude) > 0.00001) && (piLongitude - m.Longitude) < 0
        BottomRightArrow;
    end

    acceleration = readAcceleration(senseHat);
    % Along the North-South axis
    YAcceleration = acceleration(2);
    % Along the East-West axis
    XAcceleration = acceleration(1);

    % Acceleration is change in velocity over change in time
    YVelocity = YVelocity + YAcceleration * 0.5;
    XVelocity = XVelocity + XAcceleration * 0.5;

    % Velocity is change in position over change in time
    deltaYPosition = YVelocity * 0.5;
    deltaXPosition = XVelocity * 0.5;

    % USNA says that 0.11 m = 0.000001 degrees
    deltaYDegrees = 0.000001 * (deltaYPosition/0.11);
    deltaXDegrees = 0.000001 * (deltaYPosition/0.11);

    % Updating GPS coordinates
    piLatitude = piLatitude + deltaYDegrees;
    piLongitude = piLongitude + deltaXDegrees;

end

disp('You have arrived');
senseHat.displayMessage("You have arrived");
