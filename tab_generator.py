import webbrowser
import time
import random

while True:
	sites = random.choice(['reddit.com/r/python', 'reddit.com/r/cscareerquestions', 'reddit.com/r/learnprogramming', 'readcomicsonline.to', 'freecodecamp.medium.com'])
	visit = 'http://{}'.format(sites)
	webbrowser.open(visit)
	seconds = random.randrange(5, 20)
	time.sleep(seconds)
