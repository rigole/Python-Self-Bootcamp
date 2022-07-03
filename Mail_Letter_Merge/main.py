

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)
    
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    