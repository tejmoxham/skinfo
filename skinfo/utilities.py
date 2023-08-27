
import re, smtplib, ssl
from skinfo import db
from skinfo import app, config
from datetime import datetime
from email.utils import formataddr
from email.message import EmailMessage
from skinfo.models import db, Items, Subscriptions
from flask import flash, Markup, session

# ------------------------------------------------------ #
# Meta Information
# ------------------------------------------------------ #

meta = {
    'now' : datetime.utcnow()
}

# ------------------------------------------------------ #
# Retrieve Items
# ------------------------------------------------------ #

def retrieve_items(request):
    if request.method=="POST" and ("sortby" in request.form) and ("limit" in request.form):
        session["items_sortby"] = request.form["sortby"]
        session["items_limit"] = request.form["limit"]
    elif ("items_sortby" not in session) or ("items_limit" not in session):
        session["items_sortby"] = "newest"
        session["items_limit"] = 25
    sort_by = session["items_sortby"]
    limit = session["items_limit"]
    if sort_by=='alphabetical':
        items = Items.query.order_by(Items.title.asc()).limit(limit)
    elif sort_by=='newest':
        items = Items.query.order_by(Items.date_published.desc()).limit(limit)
    elif sort_by=='oldest':
        items = Items.query.order_by(Items.date_published.asc()).limit(limit)
    elif sort_by=='author':
        items = Items.query.order_by(Items.author.asc()).limit(limit)
    elif sort_by=='popularity':
        items = Items.query.order_by(Items.views.desc()).limit(limit)
    return items

# ------------------------------------------------------ #
# Email Validator
# ------------------------------------------------------ #

def email_validator(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, email):
        return True
    else:
        return False

# ------------------------------------------------------ #
# Subscription Form
# ------------------------------------------------------ #

def check_subscription_form(request):
    if request.method=="POST" and ("subscription_email" in request.form):
        email = request.form["subscription_email"]
        if email_validator(email):
            rows = Subscriptions.query.filter_by(email=email).count()
            if rows>0:
                message = Markup("<b>Success:</b> Email already subscribed to mailing list!")
                return flash(message, "flash-success")
            else:
                subscription = Subscriptions(datetime.now(), email)
                with app.app_context():
                    try:
                        db.session.add(subscription)
                        db.session.commit()
                    except Exception as e:
                        message = Markup("<b>Failure:</b> An unexpected error has occured, please try again!")
                        return flash(message, "flash-failure")
                message = Markup("<b>Success:</b> Email successfully added to mailing list!")
                return flash(message, "flash-success")
        else:
            message = Markup("<b>Failure:</b> Invalid email entered, please correct!")
            return flash(message, "flash-failure")

# ------------------------------------------------------ #
# Contact Form
# ------------------------------------------------------ #

def check_contact_form(config, request):
    if request.method=="POST" and ("contact_email" in request.form) and ("contact_name" in request.form) and "contact_message" in request.form:
        reply_email = request.form["contact_email"]
        reply_name = request.form["contact_name"]
        contact_message = request.form["contact_message"]
        # Validate Form Inputs
        if not email_validator(reply_email):
            flash_message = Markup("<b>Failure:</b> Invalid email entered, please correct!")
            return flash(flash_message, "flash-failure")
        elif len(reply_name)<3:
            flash_message = Markup("<b>Failure:</b> Invalid name entered, please correct!")
            return flash(flash_message, "flash-failure")
        elif len(contact_message)<3:
            flash_message = Markup("<b>Failure:</b> Invalid message entered, please correct!")
            return flash(flash_message, "flash-failure")
        else:
            # Send Email Message
            msg = EmailMessage()
            msg['subject'] = "Message Subject"
            msg['from'] = formataddr((reply_name, config["mail"]["email"]))
            msg['to'] = formataddr((config["mail"]["name"], config["mail"]["email"]))
            msg['reply-To'] = formataddr((reply_name, reply_email))
            msg.set_content(contact_message)
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(config["mail"]["server"], config["mail"]["port"], context=context) as smtp:
                    smtp.login(config["mail"]["username"], config["mail"]["password"])
                    smtp.sendmail(msg['from'], msg['to'], msg.as_string())
                flash_message = Markup("<b>Success:</b> Email sent successfully, we will contct you soon!")
                return flash(flash_message, "flash-success")
            except:
                flash_message = Markup("<b>Failure:</b> An unexpected error has occured, please try again!")
                return flash(flash_message, "flash-failure")