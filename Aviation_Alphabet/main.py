import pandas as pd

# creating a dictionary

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(phonetic_dict)