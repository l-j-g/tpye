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

def start():
	username = get_name()
	difficulty = select_difficulty()
	test_txt = select_test(difficulty)
	print(test_txt)
	term = Terminal()

	start=time.time()
	word_count = 0
	attempt = []
	this_word = ""




	while word_count < test_txt.count(" "):
		with term.cbreak():
			key_press = term.inkey()
			if key_press == " ":
				word_count += 1
				attempt.append(this_word)
				this_word = ""
			else: 
				this_word = this_word + key_press 
	print(attempt)
					



""" def print_test(test_txt, word):
	#init
	red = "\033[31m"
	green = "\033[32m"
	blue = "\033[34m"
	reset = "\033[39m" """

