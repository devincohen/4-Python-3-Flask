from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World, it is a bright day for the Dojo!"

@app.route('/play')
def play():
    return render_template('play_x.html', x=3, color = "blue")

@app.route('/play/<int:x>')
def play1(x):
    return render_template('play_x.html', x=x, color = "blue")


@app.route('/play/<int:x>/<string:color>')
def play2(x = 3,color = 'blue'):
    return render_template('play_x.html', x=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)

