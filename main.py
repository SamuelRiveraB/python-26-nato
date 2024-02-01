import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(alpha_dict)


def gen():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [alpha_dict[i] for i in word]
    except KeyError:
        print("Error: Only letters allowed")
        gen()
    else:
        print(nato_list)


gen()
