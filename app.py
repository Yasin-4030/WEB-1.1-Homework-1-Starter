

from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def homepage():
    """Something"""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def fav_animal(users_animal):
    """What is you favorite animal?"""
    return f'Wow! {users_animal} is also my favorite animal.'

@app.route('/dessert/<users_dessert>')
def fav_dessert(users_dessert):

    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'Where are {adjective} {noun} manufactured?.... The satisfactory.'

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        return f'{num1} times {num2} is {num1 * num2}'
    else:
        return f'Invalid input, should be numbers please'

@app.route('/sayntimes/<word>/<n>')
def ntimes(word, n):

    if n.isdigit():
        n = int(n)
        repeatedWord = ''
        for i in range(n):
            repeatedWord += " " + word
        return repeatedWord 
    else:
        return f'Invalid input, should be a word and a number please'

@app.route('/dicegame')
def dicegame():
    rnum = random.randint(1, 6)
    if rnum == 6:
        return f'You rolled a {rnum}, You Won!'
    else:
        return f'Sorry you rolled a {rnum}, You lost!'


if __name__ == '__main__':
    app.run(debug=True)