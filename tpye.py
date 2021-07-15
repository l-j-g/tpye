from functions import welcome, start_game, about, load_highscores, print_highscores

selection = welcome()

if selection == 's':
	start_game()
if selection == 'a':
	about()
if selection == "h":
	high_scores = load_highscores()
	print_highscores(high_scores)

