from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 10)


@app.route('/')
def home_page():
    return "<h1>Higher or Lower Game</h1>" \
           '<h2>Guess a number between 0 and 9<h2>' \
           '<img src="https://c.tenor.com/XpXsPDTXhYQAAAAC/math-numbers.gif">'


@app.route("/<int:guess>")
def user_guess(guess):
    print(random_num)
    if guess == random_num:
        return '<h1>Correct! You found me</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess <= random_num:
        return '<h1>Too low, try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess >= random_num:
        return '<h1>Too high, try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)
