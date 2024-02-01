import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(alpha_dict)

word = input("Enter a word: ").upper()
nato_list = [alpha_dict[i] for i in word]
print(nato_list)