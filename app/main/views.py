#3rd
from dataclasses import field
from flask import render_template, request, redirect, url_for
import requests

#local
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import FieldForm, SearchForm
import app.service.text_cloud as tc
import os

@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@main.route("/rank", methods=["GET", "POST"])
def rank():
    form = FieldForm()
    if request.method == "POST":
        if form.validate_on_submit():
            field = form.field.data
            return redirect(url_for("main.rank_field", field=field))
    return render_template("rank.html", form=form)

@main.route("/rank/<string:field>", methods=["GET"])
def rank_field(field):
    #response = requests.get(f"https://stars-api-romantic-tm.herokuapp.com/v1/rank/{field}")
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

    return render_template("rank_field.html", field = field)

@main.route("/text_cloud", methods=["GET", "POST"])
def text_cloud():
    form = FieldForm()
    if request.method == "POST":
        if form.validate_on_submit():
            field = form.field.data
            return redirect(url_for("main.text_cloud_field", field=field))
    return render_template("text_cloud.html", form=form)

@main.route("/text_cloud/<string:field>", methods=["GET"])
def text_cloud_field(field):
    #response = requests.get(f"https://stars-api-romantic-tm.herokuapp.com/v1/textcloud/{field}")
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

    return render_template("text_cloud_field.html", text_cloud = new_text_cloud, field = field)

@main.route("/cos_sim", methods=["GET", "POST"])

def cos_sim():
    field_form = FieldForm()
    search_form = SearchForm()
    if request.method == "POST":
        if (field_form.validate_on_submit() | search_form.validate_on_submit()):
            field = [field_form.field.data, search_form.keyword.data]
            return redirect(url_for("main.cos_sim_field", field=field))

    return render_template("cos_sim.html", search_form=search_form, field_form = field_form)

@main.route("/cos_sim/<string:field>", methods=["GET"])
def cos_sim_field(field):
    #response = requests.get(f"https://stars-api-romantic-tm.herokuapp.com/v1/rank/{field}")
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

    return render_template("cos_sim_field.html", field = field)