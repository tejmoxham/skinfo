
import smtplib, json
from skinfo import app, config
from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request, session
from skinfo.utilities import meta, check_subscription_form, check_contact_form, retrieve_items

# ------------------------------------------------------ #
# About & Contact
# ------------------------------------------------------ #

@app.route("/about/", methods=["GET", "POST"])
def about():

    # Check subscription POST
    check_subscription_form(request)

    return render_template("about.html", title="About", **meta)

@app.route("/contact/", methods=["GET", "POST"])
def contact():

    # Check subscription POST
    check_subscription_form(request)

    # Check contact POST
    check_contact_form(config, request)

    return render_template("contact.html", title="Contact", **meta)

# ------------------------------------------------------ #
# Items
# ------------------------------------------------------ #

@app.route("/", methods=["GET", "POST"])
def home():
    
    # Check subscription POST
    check_subscription_form(request)

    # Check sort by POST
    items = retrieve_items(request)

    return render_template("home.html", title="Items", **meta, items=items)

@app.route("/<name>/", methods=["GET", "POST"])
def item(name):

    # Check subscription POST
    check_subscription_form(request)

    return render_template("item.html", **meta)