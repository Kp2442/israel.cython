def pig_latin(word):

	first_letter=word[0]

	if first_letter in('aeiou'):
		pig_word = word + 'ay'

	else:
		pig_word = word[1:] + first_letter + 'ay'

	return pig_word

def pig_latin_decode(word):

	last_letter=word[-3]

	if last_letter in ('aeiou'):
		pig_word_decoded = word[:-2]

	else:
		pig_word_decoded = last_letter + word[:-3]

	return pig_word_decoded

word = input("Enter a word: ")
code = pig_latin(word)
print(pig_latin(word))
decode = input("Would you like to decode the word?)
if decode.lower().startswith('y'):
    	print(pig_latin_decoder(code))		       
