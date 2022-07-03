from logging import PlaceHolder


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    #print(names)
    
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)