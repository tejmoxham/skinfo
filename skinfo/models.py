
from skinfo import db
from datetime import datetime
 
# ------------------------------------------------------ #
# Items
# ------------------------------------------------------ #

class Items(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    image_path = db.Column(db.String(), nullable=True)
    author = db.Column(db.String(), nullable=True)
    date_published = db.Column(db.DateTime())
    synopsis = db.Column(db.Text(), nullable=True)
    tags = db.Column(db.String(), nullable=True)
    item_name = db.Column(db.String(), nullable=False)
    views = db.Column(db.Integer(), nullable=False)

    def __init__(self, title, image_path, author, date_published, synopsis, tags, item_name, views):
        self.title = title
        self.image_path = image_path
        self.author = author
        self.date_published = date_published
        self.synopsis = synopsis
        self.tags = tags
        self.item_name = item_name
        self.views = views

# ------------------------------------------------------ #
# Subscriptions
# ------------------------------------------------------ #

class Subscriptions(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    date_subscribed = db.Column(db.DateTime())
    email = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, date_subscribed, email):
        self.date_subscribed = date_subscribed
        self.email = email































