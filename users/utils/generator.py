import re 
from random import randint

name = 'fikrimzuadi@gmail.com'

def username_generator(name):
	email = re.sub(r'@\S*\s?', '', name)
	username = email + str(randint(0, 999))
	return username
	