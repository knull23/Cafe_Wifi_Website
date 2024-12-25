from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Cafe Model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    opening_time = db.Column(db.String(50), nullable=False)
    closing_time = db.Column(db.String(50), nullable=False)
    coffee_rating = db.Column(db.String(10), nullable=False)
    wifi_rating = db.Column(db.String(10), nullable=False)
    power_rating = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Cafe {self.name}>'
