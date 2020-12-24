'''
findMatch.py

Find the target string/substring/char in text and return the location

After testing, horsepool algorithm does not outperform the default find() function.
'''

from collections import defaultdict
def horspool_match(pattern, text):
	return text.find(pattern)


#original horsepool algorithm, no longer in use
'''
def shift_table(pattern):
	table = defaultdict(lambda: len(pattern))
	for index in range(0, len(pattern)-1):
		table[pattern[index]] = len(pattern) - 1 - index
	return table

def horspool_match(pattern, text):
	table = shift_table(pattern)
	index = len(pattern) - 1
	while index <= len(text) - 1:
		match_count = 0
		while match_count < len(pattern) and pattern[len(pattern)-1-match_count] == text[index-match_count]:
			match_count += 1
		if match_count == len(pattern):
			return index-match_count+1
		else:
			index += table[text[index]]
	return -1
'''
