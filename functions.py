from art import *
from content import *
from random import randrange

def welcome():
	tprint("tpye",font="block",chr_ignore=True)
	selection = input("(a)bout, (s)tart, (h)ighscores\n")
	return selection

def about():
	pass

def highscores():
	pass

def start():
	user_name = input("Enter your name: ")
	difficulty = input("Choose your difficulty: (b): beginner, (i): intermediate, (e): expert\n")
	if difficulty in difficulties:
		# Select the test text for the selected difficulty 
		tests = typing_tests[difficulties[difficulty]]
		# Choose a random passage of text of the selected difficulty 
		total_tests = len(tests)
		test_txt = tests[randrange(1,total_tests,1)]
		print(test_txt)