import pandas
data = pandas.read_csv("100-Days-Of-Code/100 Days/day26/nato_phonetic_alphabet.csv")
nato_alphabet =  {row.letter:row.code for (index, row) in data.iterrows()}

def generate_pheonetic():
    word = input("Enter a word: ").upper()
    try:
        list_comprehension = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_pheonetic()
    else:
        print(list_comprehension)

generate_pheonetic()