#3rd
from flask import render_template, session, redirect, url_for, current_app
import requests

#local
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import StarsForm, SearchForm
import app.service.text_cloud as tc
import os

@main.route('/', methods=['GET', 'POST'])
def index():

    field_form = StarsForm()
    #if form.validate_on_submit():

    #    return redirect(url_for('.index'))

    #dirname = os.path.dirname(__file__)
    #path = os.path.join(dirname, '../static/assets/data.json')
    #new_text_cloud = tc.AddTextCloud(path)
    #new_text_cloud.create_textcloud()
    search_form = SearchForm()
    return render_template('index.html', field_form=field_form, search_form = search_form)

@main.route("/textcloud/<string:field>", methods=["GET"])
def text_cloud(field):
    response = requests.get(f"https://stars-api-romantic-tm.herokuapp.com/v1/textcloud/{field}")
    #call api
    #render textcloud based on response
    #new_text_cloud = tc.AddTextCloud(response.json())
    #new_text_cloud.create_textcloud()
    class FakeTextCloud:
        def get_textclouds_level(self):
            levels = [
                "Platinum", "Bronze"
            ]
            return levels
    new_text_cloud = FakeTextCloud()

    return render_template('textcloud.html', text_cloud = new_text_cloud)
    #return render_template('textcloud.html', text_cloud = new_text_cloud)

