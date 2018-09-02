# README #

### What is this repository for? ###

This is a cricket simulation application.

### How do I get set up? ###

This project uses python3. You need to have 
python3.6 virtual environment installed on your machine.
To install python3.6 virtual environment follow this link:
 
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

After installing the virtual environment, go to the project folder and type: 

    source <virtual_env_directory> activate
    
Run the application by typing:
    
    python src/main.py


### How to run tests
Test cases are located in tests folder.
In order to run the test cases simply type:

    python tests/runner.py

### Project Structure and Logic

The whole code lies in the src folder. Two files handle all the code
1. main.py - This is the main starting file of the application. It creates two teams, add players and starts the game.

2. player.py - This is a player class which handles player related information like runs, balls_played, position on pitch (striker/ non-striker), etc and necessary methods for carrying out player functionality.

3. team.py - This is a team class which handles all the team related information like runs scored, active players, total players, etc and necessary methods for carrying out team functionality.

4. game.py - This is a game class and the main logic of playing the game lies here.

5. commentary.py - Handles all the commentary related logic. 

### Who do I talk to? ###

* Tarun Chaudhary (http://curioustechie.in)