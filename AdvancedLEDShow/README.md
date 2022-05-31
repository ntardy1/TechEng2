The first class project was using Raspberry Pis, breadboards, and LEDs to make some sort of LED game/show.
These are the scripts that control the reaction game I made. timerScript.py controls the LED-based timer that consisted of 15 single-color LEDs: 5 green,
5 yellow, and 5 red. RGBScript.py controls the multicolor LEDs, as well as interprets the keyboard input that, combined, made up the basis for the game. LEDThreading.py
is the script that makes the previous two run simeltaneously, which is required in order for the game to work as intended.
# Note: Problems
The LEDThreading.py script does not stop the scripts at the appropriate time. It lets them run indefinitely, which is not the intended way to play the game.
As a makeshift solution, pressing the 'esc' key will stop the LEDThreading.py script, which effectively ends the game. However, future refinement of this project
could involve making the script end its execution at the appropriate time.
