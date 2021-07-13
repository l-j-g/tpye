from art import *
from content import *
from random import randrange
import time
from blessed import Terminal

def welcome():
	tprint("tpye",font="block",chr_ignore=True)
	selection = input("(a)bout, (s)tart, (h)ighscores\n")
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
	username = get_name()
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
	print(term.clear)
	results(duration,WPM, accuracy, score)


def results(duration, WPM, accuracy, score):
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
