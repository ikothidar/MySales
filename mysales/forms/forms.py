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
from wtforms.validators import DataRequired, Length

# Local models
from mysales.config.const import GST_APPLICABILITY, PRODUCT_TYPES


class PrimarySalesForm(FlaskForm):
    gst_number = StringField(
        "GST Number", validators=[DataRequired(), Length(max=15)]
    )
    invoice_number = StringField("Invoice Number", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[DataRequired()])
    goods_details = TextAreaField("Goods Details", validators=[DataRequired()])
    hsn_code = StringField("HSN Code", validators=[DataRequired()])
    taxable_value = FloatField("Taxable Value", validators=[DataRequired()])
    gst_applicability = SelectField(
        "GST Applicable to: ", choices=GST_APPLICABILITY
    )
    gst_percentage = IntegerField("GST Percentage", validators=[DataRequired()])

    submit = SubmitField("Submit")


class SecondarySalesForm(FlaskForm):
    has_gst = BooleanField("Do you have a GST Number?", default=True)
    gst_number = StringField("GST Number", validators=[Length(max=15)])
    party_name = StringField("Party Name")
    invoice_number = StringField("Invoice Number", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[DataRequired()])
    goods_details = TextAreaField("Goods Details", validators=[DataRequired()])
    taxable_value = FloatField("Taxable Value", validators=[DataRequired()])
    product_type = SelectField("Select Product Types: ", choices=PRODUCT_TYPES)
    gst_percentage = IntegerField("GST Percentage", validators=[DataRequired()])

    submit = SubmitField("Submit")


class FetchReportForm(FlaskForm):
    start_date = DateField("Start Date: ", validators=[DataRequired()])
    end_date = DateField("End Date: ", validators=[DataRequired()])

    submit = SubmitField("Submit")
