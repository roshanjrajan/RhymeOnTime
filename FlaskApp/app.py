from flask import Flask, render_template
from flask import request
app = Flask(__name__)

#@ signifies a decorator
@app.route("/")
def main():
    #return "Welcome!"
    return render_template('index.html')

@app.route("/game/")
@app.route("/game/<word>")
def game(word=None):
    return render_template('game.html', name=word)

@app.route("/testing", methods=['POST'])
def my_form_post():
    word = None
    text = request.form['text']
    text = text.upper()
    #return text
    return render_template('game.html', word=text)

if __name__ == "__main__":
    app.run()
