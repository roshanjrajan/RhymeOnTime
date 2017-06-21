from flask import Flask, render_template
app = Flask(__name__)

#@ signifies a decorator
@app.route("/")
def main():
    #return "Welcome!"
    return render_template('index.html')

@app.route("/game")
def game():
    return render_template('game.html')

if __name__ == "__main__":
    app.run()
