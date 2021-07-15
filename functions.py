from art import *
import pickle
from content import *
from random import randrange
import time
from blessed import Terminal
from tabulate import tabulate
import os
from operator import itemgetter

def welcome():
	tprint("tpye",font="block",chr_ignore=True)
	print("A terminal based typing game.")
	print("")
	print("Enter your choice: ")
	print("A: About")
	print("S: Start")
	print("H: High Scores")
	print("")
	selection = input("")
	selection = selection[0].lower()
	return selection

def about():
	pass

def highscores():
	pass

def get_name():
	return input("Enter your name: ")

def select_difficulty():
	return input("Choose your difficulty: (b): beginner, (i): intermediate, (e): expert\n")

def select_test(difficulty):
	if difficulty in difficulties:
		# Select the test text for the selected difficulty 
		tests = typing_tests[difficulties[difficulty]]
		# Choose a random passage of text of the selected difficulty 
		total_tests = len(tests)
		test_txt = tests[randrange(1,total_tests,1)]
	return test_txt

def print_test(test_txt,word_count, attempt):

	red = "\033[31m"
	green = "\033[32m"
	blue = "\033[34m"
	reset = "\033[39m"


	split_txt = test_txt.split()
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

	while word_count < test_txt.count(" ")+1:
		with term.cbreak():
			key_press = term.inkey()
			if key_press == " ":
				word_count += 1
				attempt.append(this_word)
				this_word = ""
				print(term.clear)
				print_test(test_txt,word_count, attempt)
			else: 
				this_word = this_word + key_press 
	end = time.time()
	duration, WPM, accuracy, score = calculate_score(start, end,test_txt,attempt)
	high_score_entry = (name, score, WPM, accuracy)
	print(term.clear)
	print_results(duration,WPM, accuracy, score)
	high_scores = load_highscores()
	print( type(high_scores))

	if difficulty == 'b':
		difficulty_index = 0
	if difficulty == 'i':
		difficulty_index = 1
	if difficulty == 'e':
		difficulty_index = 2

	save_score(high_score_entry, high_scores, difficulty_index)
	print_options_end_of_game()
	return

def save_score(new_score, high_scores, difficulty_index):
	high_scores[difficulty_index].append(new_score)

	for idx,scores in enumerate(high_scores):
		scores = sorted(scores,key=itemgetter(1), reverse=True)[:10]
		high_scores[idx] = scores

	with open ('scores', 'wb') as file:
		high_scores = pickle.dump(high_scores, file)
	return 

def print_options_end_of_game():
	print("V: View High Scores")
	print("R: Reset")
	print("P: Play Again")
	print("Q: Quit")
	input()
	return


def print_results(duration, WPM, accuracy, score):
	print(f"Congratulations, you completed the test in {duration} seconds.")
	print(f"Your typing speed was: {WPM} WPM")
	print(f"Your accuracy was: {accuracy}%")
	print(f"Your total score was: {score}")

def calculate_score(start,end,test_txt,attempt):
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
	with open('scores','rb') as file:
		high_scores = pickle.load(file)	
	return high_scores

def print_highscores(high_scores):

	for idx, difficulty in enumerate(difficulties):
		print("")
		print(difficulties[difficulty].capitalize())
		print("")
		print(tabulate(high_scores[idx], headers = ['Name', 'Score', 'WPM', 'Accuracy'], tablefmt='orgtbl'))
	return




