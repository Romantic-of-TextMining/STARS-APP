#3rd
from dataclasses import field
from flask import render_template, request, redirect, url_for
import requests

#local
from config import config
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import FieldForm, SearchForm
import app.service.text_cloud as tc
import os
from app.service import cos_sim as cs

API_ROOT = config[os.getenv('FLASK_CONFIG') or 'default'].FLASK_API

@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@main.route("/function_index", methods=["GET", "POST"])
def function_index():
    return render_template("function_index.html")

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
    api_path = API_ROOT+f"v1/rank"
    params = {
        "field": field,
    }
    response = requests.get(api_path, params = params)
    rank_result = response.json()

    return render_template("rank_field.html", field = field, rank_result = rank_result)

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
    api_path = API_ROOT+f"v1/textcloud"
    params = {
        "field": field,
    }
    response = requests.get(api_path, params = params)
    result_dict = response.json()
    result = tc.GenerateTfIdfTag.transform_tag(result_dict)
    return render_template("text_cloud_field.html", field = field, result = result)

@main.route("/cos_sim", methods=["GET", "POST"])
def cos_sim():
    search_form = SearchForm()
    if request.method == "POST":
        if (search_form.validate_on_submit()):
            field = search_form.field.data
            query = search_form.query.data
            return redirect(url_for("main.cos_sim_field", field=field, query = query))

    return render_template("cos_sim.html", search_form=search_form)

@main.route("/cos_sim/<string:field>/<string:query>", methods=["GET"])
#http://127.0.0.1:3030/cos_sim/en_14_participation_in_public_policy/condit
def cos_sim_field(field, query):
    api_path = API_ROOT+f"v1/cos_sim"
    params = {
        "field": field,
        "query": query
    }
    response = requests.get(api_path, params = params)
    result = response.json()

    field_result = params["field"].replace("_", " ")

    score_object = cs.CosSimResult(result)
    score = score_object.get_view_dict()
    return render_template("cos_sim_field.html", score = score, field = field_result)