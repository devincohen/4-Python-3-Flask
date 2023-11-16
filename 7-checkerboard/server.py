from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

@app.route('/')
def basic():
    return render_template('checkers.html', width=8, height=8, color1=black, color2=red)

@app.route('/<int:height_of>')
def height(height_of):
    return render_template('checkers.html', width=8, height=height_of)

@app.route('/<int:height_of>/<int:width>')
def height_width(width, height_of):
    return render_template('checkers.html', height=height_of, width=width)

@app.route('/<int:height>/<int:width>/<string:color1>/<string:color2>')
def hwcolor(height, width, color1, color2):
    return render_template('checkers.html', height=height, width=width, color1=color1, color2=color2)


if __name__=='__main__':
    app.run(debug=True)