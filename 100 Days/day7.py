import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(hangman_art.logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])