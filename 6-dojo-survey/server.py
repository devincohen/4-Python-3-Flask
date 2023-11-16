from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "lovely night we're having"

@app.route('/')
def home():
    return render_template('survey.html')


@app.route('/survey', methods=['POST'])
def survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['color'] = request.form.get('color')
    session['here_for'] = request.form.get('here_for')
    session['here_for2'] = request.form.get('here_for2')

    return redirect('/success')

@app.route('/success')
def success():    
    return render_template('show.html')



if __name__=='__main__':
    app.run(debug = True)