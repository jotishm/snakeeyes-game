from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    #return render_template('page/home.html')
    return "Hello World"

@page.route('/terms')
def terms():
    #return render_template('page/terms.html')
    return "Hello from terms"

@page.route('/privacy')
def privacy():
    return "privacy page rendering"