from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user='Jost')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        flash(f'Login requested for user {login_form.username.data}, remember_me={login_form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form)
