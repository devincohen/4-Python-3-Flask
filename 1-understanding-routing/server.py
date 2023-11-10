from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    if type(name) == str:
        return f"Hi, {name.capitalize()} ;)"
    else:
        return f"Nice try. {name} is actually a {type(name)} and it needs to be a string."

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(phrase, num):
    if type(num) != int:
        return f"Nice try. {num} is actually a {type(num)} and it needs to be an integer."
    elif type(phrase) != str:
        return f"Nice try. {phrase} is actually a {type(phrase)} and it needs to be a string."
    else:
        return f"{phrase.capitalize() * num}. {num} times!"


# flask exception handling code from https://pythonprogramming.net/flask-error-handling-basics/
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
