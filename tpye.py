from functions import welcome, start, about, highscores
selection = welcome()


if selection == 's':
	start()
if selection == 'a':
	about()
if selection == "h":
	highscores()