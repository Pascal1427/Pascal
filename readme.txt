Project Fundametals of Python I719
Student: Pascal Tietjen
Class: C21 Erasmus Student

Description: A Snake Game
The project is a snake game like the first games of the old Nokia mobile phones. The goal is to be alive with the snake as long it is possible. To grow up and get faster you have to eat the food which appears as a blue block randomly.

Settings and Control:
As you wish you can edit the settings and controls in the source code. It is the first block after the imports. You can modify how fast the snake is, how big the map is and the colors from everything.

Imports:
There are 4 imports used.
1. the pygame: Pygame is a cross-platfrom library designed to make it easy to write multimedia software, such as games, in Python. Pygame requires the Python language and SDL multimedia library. It can also make use of several other popular libraries. ("http://www.pygame.org/readme.html") if you dont have it please install it with python 2.7.
2. the random: This module implements pseudo-random number generators for various distributions.
For integers, uniform selection from a range. ("https://docs.python.org/2/library/random.html")
3. the unittest: The Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language. ("https://docs.python.org/2/library/unittest.html")
4. the sys libary: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.("https://docs.python.org/2/library/sys.html")

Let's beginn:
Open the file snake_game_pascal_tietjen.py with a python interpreter. Now you will see the start screen with a map. To start press any key except the the 't' because this one is a spare for the test. To control the snake use the [Arrow] keys like the signs on it. If you started the snake will go to the right of the map. Locate the food and try to eat it. When you got it the snake will grow up one stone and get a little bit faster. Repeat this as long you can. If you hit the wall or yourself, the game will be over.

Test it:
To test the funktion Inc_L() from the snake class the unittest was used. It checks that function is working and increased the length of the snake. After this it will show you the test in the console with the time state.
