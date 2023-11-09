# type: ignore

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'} # dictionary

while True:
    user_input = input("Enter the string to translate, or type '-q' to quit. ")
    user_input = user_input.upper() # change lowercase to uppercase
    if user_input == "-Q": # uppercase because of the previous line
        break # if you input q it quits
    morse_translation = ""
    translation_good = True # flag to be set if we hit an unknown character
    for letter in user_input:
        if letter == " ":
            morse_translation += "/" # a space in the input translates to a break or "/" in morse
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " " # for spaces between characters
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") # if there's an error type this
                translation_good = False
                break # go to next line
    if translation_good:
        print(morse_translation) # if nothing goes wrong print the translation