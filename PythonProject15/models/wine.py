from utils.db import db

class Wine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fixed_acidity = db.Column(db.Float, nullable=False)
    volatile_acidity = db.Column(db.Float, nullable=False)
    citric_acid = db.Column(db.Float, nullable=False)
    residual_sugar = db.Column(db.Float, nullable=False)
    chlorides = db.Column(db.Float, nullable=False)