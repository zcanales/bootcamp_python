import sys
import string

def text_analyzer(text = ""):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    text_analyzer.char = 0;
    text_analyzer.upper = 0;
    text_analyzer.lower = 0;
    text_analyzer.punct = 0;
    text_analyzer.space = 0;
    for c in text:
        if c.isupper():
            text_analyzer.upper += 1
            text_analyzer.char += 1
        elif c.islower():
            text_analyzer.lower += 1
            text_analyzer.char += 1
        elif c.isspace():
            text_analyzer.space += 1
            text_analyzer.char += 1
        elif c in string.punctuation:
            text_analyzer.punct += 1
            text_analyzer.char += 1
    if text_analyzer.char == 0:
        print("Your text is empty.")
    else:
        print("The text contains " + str(text_analyzer.char) + " characters")
        print("- " + str(text_analyzer.upper) + " upper letters")
        print("- " + str(text_analyzer.lower) + " lower letters")
        print("- " + str(text_analyzer.punct) + " punctuation marks")
        print("- " + str(text_analyzer.space) + " spaces")

#if (len(sys.argv) == 1 or len(sys.argv) == 0)  :
#	print("You should enter a text to analyse in the command line")
#elif len(sys.argv) > 2:
#	print("Please enter only one text to analyse")
#else:
#	text_analyzer(sys.argv[1])
