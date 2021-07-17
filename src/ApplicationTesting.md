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

### 
