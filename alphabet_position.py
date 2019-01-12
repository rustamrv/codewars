def alphabet_position(text):
    output = ""
    for ch in text:
        if ch.isalpha(): 
            if len(output) == 0:
               output += str(ord(ch.lower())-96) 
            else:   
               output += " " + str(ord(ch.lower())-96)
    return output
