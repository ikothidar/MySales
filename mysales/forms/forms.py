# Flask modules
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    FloatField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, NumberRange

FETCH_OPTIONS = [
    ("both", "Both"),
    ("secondary", "Secondary Sales"),
    ("primary", "Primary Sales"),
]


class PrimarySalesForm(FlaskForm):
    gst_number = StringField(
        "GST Number", validators=[DataRequired(), Length(max=15)]
    )
    invoice_number = StringField("Invoice Number", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[DataRequired()])
    goods_details = TextAreaField("Goods Details", validators=[DataRequired()])
    hsn_code = StringField("HSN Code", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])
    gst_percentage = IntegerField("GST Percentage", validators=[DataRequired()])

    submit = SubmitField("Submit")


class SecondarySalesForm(FlaskForm):
    has_gst = BooleanField('Do you have a GST Number?', default=True)
    gst_number = StringField("GST Number", validators=[Length(max=15)])
    party_name = StringField("Party Name")
    invoice_number = StringField("Invoice Number", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[DataRequired()])
    goods_details = TextAreaField("Goods Details", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])
    gst_percentage = IntegerField("GST Percentage", validators=[DataRequired()])

    submit = SubmitField("Submit")


class FetchReportForm(FlaskForm):
    fetch_type = SelectField('Report Fetch Type: ', choices=FETCH_OPTIONS)
    start_date = DateField("Report Month: ", validators=[DataRequired()])
    end_date = DateField("Report Year: ", validators=[DataRequired()])

    submit = SubmitField("Submit")
