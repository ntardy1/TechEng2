# FindMy
The idea with this project was to make a system similar to that of Apple's 'Find My' feature, which allows a user to use their Apple device's Bluetooth capablilities to
find help locate a lost device. The main.m file is the primary script, and it contains all of the GPS processing and mathematical procedures that help the project work.
# Problems
The acceleration readings from the Raspberry Pi's sense hat were very inconsistent. For example, the RPi could be at rest, and yet the acceleration readings would still
be non-zero. Also, if the RPi was left at rest in two different locations, the acceleration readings would differ as well. For these reasons, the primary goal of the 
project was never fully achieved. Given more consistent acceleration measurements, this could be a very viable project.
