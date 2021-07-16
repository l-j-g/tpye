from functions import *
quit = False
selection = welcome()

while quit == False:
	if selection == 's':
		start_game()
		selection = print_options_end_of_game()
	if selection == 'a':
		about()
	if selection == "v":
		high_scores = load_highscores()
		print_highscores(high_scores)
		selection = high_scores_menu()
	if selection == 'q':
		quit = True
	if selection == 'b':
		selection = welcome()



