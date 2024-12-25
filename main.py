# main.py
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from models import db, Cafe

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Extensions
Bootstrap5(app)
db.init_app(app)

# Create Database Tables
with app.app_context():
    db.create_all()
    print("Database created successfully!")


# Home Route
@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)


# Add Cafe Route
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        opening_time = request.form.get('opening_time')
        closing_time = request.form.get('closing_time')
        coffee_rating = request.form.get('coffee_rating')
        wifi_rating = request.form.get('wifi_rating')
        power_rating = request.form.get('power_rating')

        new_cafe = Cafe(
            name=name,
            location=location,
            opening_time=opening_time,
            closing_time=closing_time,
            coffee_rating=coffee_rating,
            wifi_rating=wifi_rating,
            power_rating=power_rating
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash('Cafe added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add.html')


# Display Cafes Route
@app.route('/cafes')
def cafes():
    all_cafes = Cafe.query.all()
    return render_template('cafes.html', cafes=all_cafes)


# Delete Cafe Route
@app.route('/delete/<int:cafe_id>', methods=['POST'])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    flash('Cafe deleted successfully!', 'success')
    return redirect(url_for('cafes'))


if __name__ == '__main__':
    app.run(debug=True)
