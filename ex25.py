#breaks up words
def break_words(stuff):
	words = stuff.split(' ')
	return words

#sorts the words
def sort_words(words):
	return sorted (words)

#prints the first word after popping it off
def print_first_word(words):
	word = words.pop(0)
	print word

#prints the last word after popping it off
def print_last_word(words):
	word = words.pop(-1)
	print word

#takes in full sentence and returns the sorted words
def sort_sentences(sentence):
	words = break_words(sentence)
	return sort_words(words)

#prints the first and last words of the sentence
def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
#sorts the words then prints out the first and last word
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
        print_first_word(words)
        print_last_word(words)

