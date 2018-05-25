from flask import render_template, flash, redirect, url_for
from . import main
from .. import db
from .forms import LoginForm


@main.route('/')
def index():
    """Default application route."""
    form = LoginForm()
    return render_template('index.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
