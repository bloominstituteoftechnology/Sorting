#!/usr/bin/env python


# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 8
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


def print_divisible_by_3(array):
	new_array = [value for value in array if value % 3 == 0]
	for item in new_array:
		print(item)


print_divisible_by_3(array)


# Print out all of the strings in the following array that represent a number divisible by 3:
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine,
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


number_words = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9,

	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'thirteen': 13,
	'fourteen': 14,
	'fifteen': 15,
	'sixteen': 16,
	'seventeen': 17,
	'eighteen': 18,
	'nineteen': 19,

	'twenty': 20,
	'thirty': 30,
	'forty': 40,
	'fifty': 50,
	'sixty': 60,
	'seventy': 70,
	'eighty': 80,
	'ninety': 90,
}


def interpret_number_words(text):
	total = 0
	words = text.split(' ')
	word_iterator = iter(words[::-1])
	for word in word_iterator:
		if word in number_words:
			total += number_words[word]
		elif word == 'hundred':
			word = next(word_iterator)
			if word not in number_words:
				raise ValueError
			total += 100 * number_words[word]
		else:
			raise ValueError
	return total


number_texts = [
	"five",
	"twenty six",
	"nine hundred ninety nine",
	"twelve",
	"eighteen",
	"one hundred one",
	"fifty two",
	"forty one",
	"seventy seven",
	"six",
	"twelve",
	"four",
	"sixteen",
]


numbers = [
	interpret_number_words(number_text)
	for number_text in number_texts
]


for number, text in zip(numbers, number_texts):
	if number % 3 == 0:
		print(text)

