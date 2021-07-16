from functions import *
from sys import argv
quit = False

try: 
	if argv[1] == "--help" or "--h":
		selection = 'a'
	if argv[1] == "--start":
		selection = 's'
	if argv[1] == "--highsocres":
		pass
	if argv[1] == "--version":
		pass
except IndexError:
		selection = welcome()


while quit == False:
	if selection == 's':
		start_game()
		selection = print_options_end_of_game()
	if selection == 'a':
		selection = about()
	if selection == "v":
		high_scores = load_highscores()
		print_highscores(high_scores)
		selection = high_scores_menu()
	if selection == 'q':
		quit = True
	if selection == 'b':
		selection = welcome()
	if selection == 'a':
		selection = about() 



