from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm
from . import text_cloud
import os

@main.route('/', methods=['GET', 'POST'])
def index():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../static/assets/data.json')
    new_text_cloud = text_cloud.AddTextCloud(path)
    new_text_cloud.create_textcloud()
    return render_template('index.html')
