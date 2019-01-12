#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.


def alphabet_position(text):
    output = ""
    for ch in text:
        if ch.isalpha(): 
            if len(output) == 0:
               output += str(ord(ch.lower())-96) 
            else:   
               output += " " + str(ord(ch.lower())-96)
    return output
