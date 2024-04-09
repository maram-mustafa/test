from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(128), index=True)
    item_price = db.Column(db.Float)
    item_image = db.Column(db.String(256))
    item_description = db.Column(db.Text)