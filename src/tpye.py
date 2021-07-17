from functions import *
from sys import argv
quit = False

try: 
	if argv[1] == "--help":
		with open('help.md', 'r') as f:
			text = f.read()
			print(text)
			quit = True
	if argv[1] == "--start":
		selection = 's'
	if argv[1] == "--highscores":
		selection = 'v'
	if argv[1] == "--about":
		selection = 'a'
	if argv[1] == "--version":
		print(argv[1])
		print("tpye version 1.0")
		quit = True
except IndexError:
		selection = welcome()

while quit == False:
	if selection == 's':
		start_game()
		selection = print_options_end_of_game()
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



