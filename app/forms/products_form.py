from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    submit = SubmitField("Submit")
