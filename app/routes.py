from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    state = {'state': 'initial'}
    return render_template('index.html', title='Home', state=state)


@app.route('/state_01')
def state_01():
    state = {'state': 'state_01'}
    return render_template('state_01.html', title='State_01', state=state)


@app.route('/state_02')
def state_02():
    state = {'state': 'state_02'}
    return render_template('state_02.html', title='State_02', state=state)


@app.route('/state_03')
def state_03():
    state = {'state': 'state_03'}
    return render_template('state_03.html', title='State_03', state=state)


@app.route('/state_04')
def state_04():
    state = {'state': 'state_04'}
    return render_template('state_04.html', title='State_04', state=state)


