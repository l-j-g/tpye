# Tpye : Application Testing 

## Dynamic Highlighting 

This test procedure will test if the dynamic highlighting feature of the application is working correctly. This feature is expected to highlight the current word being typed in the color blue and previously typed words in either red or green, depending if they were typed correctly. 

Test Cases: 

### 1 - Difficulty setting (beginner,intermediate,expert)

Expected behavior: The dynamically highlighting should work as intended for each of the possible difficulty settings.

Observations: The feature is working as intended. For longer passages of text (e.g. expert setting) the terminal display may flicker when new words are entered.  

### 2 - Special Characters

Expected behavior: 
- Typing non-alphanumeric characters such as the enter key should not affect the text marking or spelling of words.
- Typing backspace key should remove the last character of the typed word.
- Typing spacebar key should end the current word, indicate if the previously typed words were spelled correctly and highlight word currently being typed in blue.
- Terminal interrupt and flow control characters should be unaffected (i.e Ctrl + C should end the application)

Observations: The feature is working as intended. When pressing the backspace key on some terminal emulators the text prompt will be moved backwards but the character will not be removed until it has been replaced with a new character. This is a visual bug that does not affect performance.

### 3 Empty Strings / Error checking 

Expected behavior: 

- Empty strings (pressing spacebar without entering any characters) should mark the current word as incorrect and move the currently tpyed word to the next word.
- Words that are typed correctly should get highlighted in green. 
- Words that are typed incorrectly should get highlighted in red.
- The current word being typed should get highlighted in blue.

Observations: The feature is working as intended.

## High Scores / Score Calculation

### No words are spelt correctly

Expected behavior: If no words are typed correctly, the words per minute should be the number of words typed per minute. The accuracy should be 0% and the score should be zero.

Observations: The feature is mostly working as intended, with a minor bug observed - if the user only presses spacebar and makes no attempt at typing any words program will count empty strings as words. Technically, empty strings are not words. This is addressed in the total score calculate which multiplies the number of words typed by the accuracy - therefore someone who enters only empty strings will recieve a low score due to low accuracy.  

### Highscore file is deleted from disk. 
Expected behavior: 
If the 'scores' file is removed from the installation the following behavior is expected: 
If the user tries to view highscores, an error message is displayed stating the no high scores has been found. 
If a new game is played, a new 'scores' file is created and the highscore is displayed at the end of the game. 

Observations: The feature is working as intended. If the scores file is removed by the user the error is handled gracefully and a new file will be created. 

### New Highscore

Expected behavior: 
After a game is completed, if the score is in the top 10 high scores for that difficulty, the user will be notified and the score will be added to the list of high scores.

Observations: The feature is working as intended. The user is notified and only the top 10 highscores for each difficulty is displayed. 

