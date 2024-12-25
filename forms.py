from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    opening_time = StringField('Open', validators=[DataRequired()])
    closing_time = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['✘', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')
