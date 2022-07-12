import pandas as pd

# creating a dictionary

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(phonetic_dict)

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]

print (output_list)