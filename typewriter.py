import sys
import time

def typewriter(message):
#	print(message)
	for char in message:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.03)