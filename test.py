import pickle
from operator import itemgetter


high_scores_beginner = [
	("Jack", 300, 30, 80),
	("Louie", 9000, 30, 80),
	("Jack", 3000, 30, 80)
]
high_scores_intermediate = [
	("Gin", 6000, 30, 80),
	("Jack", 9000, 30, 80),
	("James", 2000, 30, 80)
] 
high_scores_expert = [
	("John", 300, 30, 80),
	("Joe", 5000, 30, 80),
	("Jack", 6000, 30, 80)
]
high_scores = [high_scores_beginner,high_scores_intermediate,high_scores_expert]

print(high_scores)
print("-----")

for idx,scores in enumerate(high_scores):
	print(scores)
	scores = sorted(scores,key=itemgetter(1), reverse=True)[:10]
	high_scores[idx] = scores
	print(scores)
	print('-----')

print(high_scores)
with open ('scores', 'wb') as file: 
	pickle.dump(high_scores, file)

high_scores = []

with open('scores','rb') as file:
	high_scores = pickle.load(file)
print(high_scores)
