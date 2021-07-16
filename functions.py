from art import *
import pickle
from content import *
from random import randrange
import time
from blessed import Terminal
from tabulate import tabulate
from operator import itemgetter

def welcome():
	tprint("tpye",font="block",chr_ignore=True)
	print("A terminal based typing game written in python.")
	print("")
	print("Enter your choice: ")
	print("A: About this application")
	print("S: Start a new game")
	print("V: View High Scores")
	print("Q: Quit application")
	selection = input("")
	try: 
		selection = selection[0].lower()

		if selection == "a" or selection == "s" or selection == "v" or selection == 'q':
			return selection
		else:
				print("That was not a valid selection. Please try again:") 
				return welcome()
	except:
		print("That was not a valid selection. Please try again:") 
		return welcome()


def about():
	tprint("tpye",font="block",chr_ignore=True)
	print("\"tpye\" is a terminal based typing game written in python.")
	print("The purpose of this game is to help develop typing skills in an enjoyable and interactive way.")
	print("The game features three difficulty settings, dynamic text highlighting and a peristent scoreboard.")
	print("Once starting the game you will be asked to type a passage of text as quickly and accurately as possible.")
	print("")
	print("Choose what you would like to do:")
	selection = input("(S): Start game, (B): Back, (Q): Quit\n")
	try: 
		selection = selection[0].lower()
		if selection == "b" or selection == "s" or selection == 'q':
			return selection
		else:
			print("That was not a valid selection. Please try again:") 
			return about()
	except:
			print("That was not a valid selection. Please try again:") 
			return about()


def get_name():
#this function take user input for their name - to identify high scores.
	return input("Enter your name: ")

def select_difficulty():
#this function takes user input to select the difficulty of the typing test.
	selection = input("Choose your difficulty: (b): beginner, (i): intermediate, (e): expert\n")
	try:
		selection = selection[0].lower()

		if selection == "b" or selection == "i" or selection == "e":
			return selection
		else:
			print("That was not a valid selection. Please enter the difficulty you would like to attempt:") 
			return select_difficulty()
	except:
		print("That was not a valid selection. Please enter the difficulty you would like to attempt:") 
		return select_difficulty()


def select_test(difficulty):
#this function randomly picks a passage of text of the selected difficulty 
	if difficulty in difficulties:
		# Select the test text for the selected difficulty 
		tests = typing_tests[difficulties[difficulty]]
		# Choose a random passage of text of the selected difficulty 
		total_tests = len(tests)
		test_txt = tests[randrange(1,total_tests,1)]
	return test_txt

def print_test(test_txt,word_count, attempt):
# this function prints the text that the user is required to type. The current word that the user is typing is highlighted with blue. Previous words that are typed are highlighted either green or red - depending if they have been spelt correctly.
	# these are ANSI escape code colours used to highlight text in the terminal.
	red = "\033[31m"
	green = "\033[32m"
	blue = "\033[34m"
	reset = "\033[39m"

	print("Type the following passage of text as quickly as possible!: ")
	split_txt = test_txt.split() #the test text is split into individual words to allow for specific highlighting of words.
	if word_count > 0:
		for index, word in enumerate(attempt):
			if word == split_txt[index]:
				split_txt[index] = green + split_txt[index] + reset
			else:
				split_txt[index] = red + split_txt[index] + reset

	if word_count < len(split_txt):
		split_txt[word_count] = blue + split_txt[word_count] + reset

	test_txt = " ".join(split_txt)
	print(test_txt)
	return 

def start_game():
# the primary function of my application that initiates a typing test 
	term = Terminal()
	name = get_name()
	difficulty = select_difficulty()
	test_txt = select_test(difficulty)
	start=time.time()

	word_count = 0
	attempt = []
	this_word = ""
	print(term.clear)
	print_test(test_txt,word_count, attempt)
#the cbreak and inkey functions from the 'blessed' package are used to capture input as it is typed. 
	while word_count < test_txt.count(" ")+1:
		with term.cbreak():
			key_press = term.inkey()
			if key_press == " ": #when spacebar is pressed this indicates that a word has been completed 
				word_count += 1
				attempt.append(this_word) #the typed word is added to a list of all typed words
				this_word = ""
				print(term.clear)
				print_test(test_txt,word_count, attempt) # this function updates the text highlighting 
			else: 
				this_word = this_word + key_press #if a other than whitepsace is entered this character is added as part of the current word that is being typed.
	end = time.time()
	duration, WPM, accuracy, score = calculate_score(start, end,test_txt,attempt)
	high_score_entry = (name, score, WPM, accuracy)
	print(term.clear)
	print_results(duration,WPM, accuracy, score)
	high_scores = load_highscores()

	if difficulty == 'b':
		difficulty_index = 0
	if difficulty == 'i':
		difficulty_index = 1
	if difficulty == 'e':
		difficulty_index = 2

	save_score(high_score_entry, high_scores, difficulty_index)
	return

def save_score(new_score, high_scores, difficulty_index):
#this function adds the high score the list of highscores, then sorts the list by score and saves the top 10 scores to the disk in binary format using the pickle library
	high_scores[difficulty_index].append(new_score)

	for idx,scores in enumerate(high_scores):
		scores = sorted(scores,key=itemgetter(1), reverse=True)[:10]
		if new_score in scores:
			print(f"Congratulations, that was the #{scores.index(new_score)} highest score for this difficulty!")
		high_scores[idx] = scores

	with open ('scores', 'wb') as file:
		high_scores = pickle.dump(high_scores, file)
	return 

def print_options_end_of_game():
# this function prompts the user for input at the end of a typing test.
	print("")
	print("V: View High Scores")
	print("S: Start Again")
	print("Q: Quit")
	selection = input()
	try: 
		selection = selection[0].lower()
		if selection == "v" or selection == "s" or selection == "q":
			return selection
		else:
				print("That was not a valid selection. Please try again:") 
				return print_options_end_of_game()
	except: 
		print("That was not a valid selection. Please try again:") 
		return print_options_end_of_game()
	


def print_results(duration, WPM, accuracy, score):
# this function prints the calculated score after a typing test is completed.
	print(f"Congratulations, you completed the test in {duration} seconds.")
	print(f"Your typing speed was: {WPM} WPM")
	print(f"Your accuracy was: {accuracy}%")
	print(f"Your total score was: {score}")

def calculate_score(start,end,test_txt,attempt):
#this function calculates the score, words per minute and accuracy after a typing test is completed 
	correct = 0
	incorrect = 0
	duration = round(end-start)
	WPM = round((len(attempt)/duration)*60)
	for index, word in enumerate(test_txt.split()):
		if word == attempt[index]:
			correct += 1
		else: 
			incorrect += 1
	accuracy = round((correct/len(test_txt.split())) * 100)
	score = accuracy * WPM

	return duration, WPM, accuracy, score

def load_highscores():
# this function loads the binary file that holds highscores using the pickle library
	with open('scores','rb') as file:
		high_scores = pickle.load(file)	
	return high_scores

def print_highscores(high_scores):
# this function prints the highscores for each difficulty in a formated table using the tabulate package
	for idx, difficulty in enumerate(difficulties):
		print("")
		print(f" Top 10 {difficulties[difficulty].capitalize()} Scores: ")
		print("")
		print(tabulate(high_scores[idx], headers = ['Name', 'Score', 'WPM', 'Accuracy (%)'], tablefmt='orgtbl'))
	return

def high_scores_menu():
#this function prompts the user for a selection after the high scores are displayed
	print("")
	print("Enter your choice: ")
	print("A: About this application")
	print("S: Start a new game")
	print("B: Go back")
	selection = input()
	try: 
		selection = selection[0].lower()
		if selection == "a" or selection == "s" or selection == "b":
			return selection
		else:
			print("That was not a valid selection. Please try again:") 
			return high_scores_menu()
	except:
			print("That was not a valid selection. Please try again:") 
			return high_scores_menu()




