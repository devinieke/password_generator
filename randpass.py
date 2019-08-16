import random

chars = '1234567890abcdefghijklmnopqrstuvwxyz!?.,-'

times = input('how many passwords do you want?')
times = int(times)

length = input('how many characters for your password(s)?') # receive input and assign to length
length = int(length) #convert input to whole number

for p in range(times):
	password = ''
	for c in range(length):
		password += random.choice(chars) #random char stored in password variable
	print(password)