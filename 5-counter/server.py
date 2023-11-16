from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "poop in the diaper"

@app.route('/')
def home():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] = int(session.get('visits')) + 1
    if 'counter' not in session:
        session['counter'] = '0'
    return render_template('home.html', visits = session.get('visits'), counter = session.get('counter'))

@app.route('/count2')# methods=['POST'])
def add():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] = int(session.get('visits')) + 1
    if 'counter' not in session:
        session['counter'] = '0'
    else:
        session['counter'] =  int(session.get('counter')) + 2  
    return render_template('home.html', counter=session['counter'], visits=session['visits']) 

@app.route('/count', methods=['POST'])
def count():
    session['increment'] = request.form['increment']
    session['result'] = int(session.get('counter')) + int(session.get('increment'))
    session['counter'] = int(session.get('result'))
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug = True)
