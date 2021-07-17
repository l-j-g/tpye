# Tpye Help File 

## Installation 

To download the source code of the application type the following command:   
`git clone https://github.com/l-j-g/tpye.git`  

## Requirements:

This program runs on Python. To install Python, check out https://installpython3.com/' 

*Tpye* requires the following python packages to be installed:

- art
- blessed
- tabulate
- strip_ansi

Before starting the application ensure that all of the system environment requirements have been met.
 
To install the necessary dependencies, navigate to your *type* src folder and execute the following command in your command line prompt:

`-pip3 install ./requirements.txt`

Ensure that the tpye executable file has the required permissions:  
`chmod +x ./type.sh`  

To start the application type the following, within the type src directory.

`./type.sh`  

## Features

### Variable Difficulty

The user can select a difficulty setting at the start of the application. The application will have three different difficulty settings (beginner, intermediate and expert). The difficulty variable will select a passage of text for the user to type from a nested dictionary stored within the application. Harder difficulties will require the user to type longer and more gramatically intensive passages of text.

All typing tests used in this program have been sourced from [[https://thepracticetest.com/typing/tests/practice-paragraphs/]] and its Authors. I take no credit for developing this material.

### Text Highlighting
  
As the user types the required passage of text, the characters input will be captured and stored in a variable. Once a word has been completed the word will be saved to a list of words typed by the user.

The display will dynamically highlight the current word that the user is attempting to type in the color blue and will highlight previously typed words in either green or red depending on if it was typed correctly.

### Score Calculation

Once the user has completed the passage of text the application will calculate a score based on the amount of the time user took to complete the test and the number of words they spelt correctly.

The top 10 scores for each difficulty will be stored on persistent file that will be saved between executions of the application. Each score will be identified by a input name provided to the application.  

## Optional Parameters

The application can be launched with the following optional arguments: 

`usage: tpye.sh [--COMMAND]`  
`optional arguments: `  
`--help : show this message and exit`  
`--start : immediately start application, skipping menus`  
`--about : display a brief description of the application`  
`--highscores : display previous players highscores`  
`--version : print the current version of the application and exit`  