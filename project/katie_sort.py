import sys
import random
import time

def katiesort(books):
	empty = []

	for a in range(ord('A'), ord('Z') + 1): # O(26) == O(1)
		for b in books: # O(n)
			if b[0] == chr(a): # O(1)
				empty.append(b)  # O(1)

	return empty


def reps(count, size):
	books = []

	# Make random books
	for i in range(size):
		books.append(chr(random.randint(ord('A'), ord('Z'))))

	start = time.time()

	# Sort a bunch of times
	for i in range(count):
		katiesort(books)

	finish = time.time()

	print("%d,%.10f" % (size, finish - start))

random.seed()

for l in range(10,11000,1000):
	reps(100, l)
