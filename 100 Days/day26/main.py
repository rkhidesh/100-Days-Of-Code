import pandas
data = pandas.read_csv("100-Days-Of-Code/100 Days/day26/nato_phonetic_alphabet.csv")
neto_alphabet =  {row.letter:row.code for (index, row) in data.iterrows()}


word = input("Enter a word: ").upper()
list_comprehension = [neto_alphabet[letter] for letter in word]
print(list_comprehension)

