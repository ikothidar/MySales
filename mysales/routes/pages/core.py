# Flask modules
from flask import Blueprint, render_template
from flask_login import login_required

# Local Modules
from mysales.config.const import PRIMARY_VALID_FIELDS, SECONDARY_VALID_FIELDS
from mysales.extensions import db
from mysales.models.models import PrimarySales, SecondarySales
from mysales.forms.forms import (
    FetchReportForm,
    PrimarySalesForm,
    SecondarySalesForm,
)
from mysales.utils.fetch_data import FetchData
from mysales.utils.models import get_name_by_gst

core_bp = Blueprint("core", __name__, url_prefix="/sales")


@core_bp.route("/fetch", methods=["GET", "POST"])
@login_required
def fetch_report_route():
    form = FetchReportForm()

    if form.validate_on_submit():
        form_data = form.data
        fetch_obj = FetchData(
            fetch_type=form_data['fetch_type'],
            start_date=form_data['start_date'],
            end_date=form_data['end_date']
        )

        fetch_obj.create_workbook()

    return render_template("pages/fetch_report.html", form=form)


@core_bp.route("/primary", methods=["GET", "POST"])
@login_required
def primary_sales_route():
    form = PrimarySalesForm()

    if form.validate_on_submit():
        form_data = form.data
        primary_obj = PrimarySales()

        gst_number = form_data.get('gst_number')

        if gst_number:
            form_data['party_name'] = get_name_by_gst(gst_number=gst_number)
        else:
            form_data['gst_number'] = 'CASH INVOICE'

        tax_amount = round(
            int(form_data['amount']) * int(form_data['gst_percentage']) / 100, 2
        )
        form_data['tax_amount'] = tax_amount
        form_data['total_bill'] = (
            int(form_data['amount']) + round(tax_amount + 0.01, 0)
        )

        for field_name, field_value in form_data.items():
            if field_name in PRIMARY_VALID_FIELDS:
                setattr(primary_obj, field_name, field_value)

        db.session.add(primary_obj)
        db.session.commit()

        return 'Data Stored successfully!'

    return render_template("pages/primary_sales.html", form=form)


@core_bp.route("/secondary", methods=["GET", "POST"])
@login_required
def secondary_sales_route():
    form = SecondarySalesForm()

    if form.validate_on_submit():
        form_data = form.data
        secondary_obj = SecondarySales()

        gst_number = form_data.get('gst_number')

        if gst_number:
            form_data['party_name'] = get_name_by_gst(gst_number=gst_number)
        else:
            form_data['gst_number'] = 'CASH INVOICE'

        tax_amount = round(
            int(form_data['amount']) * int(form_data['gst_percentage']) / 100, 2
        )
        form_data['tax_amount'] = tax_amount
        form_data['cgst'] = tax_amount / 2
        form_data['sgst'] = tax_amount / 2
        form_data['total_bill'] = (
            int(form_data['amount']) + round(tax_amount + 0.01, 0)
        )

        for field_name, field_value in form_data.items():
            if field_name in SECONDARY_VALID_FIELDS:
                setattr(secondary_obj, field_name, field_value)

        db.session.add(secondary_obj)
        db.session.commit()

        return 'Data Stored successfully!'

    return render_template("pages/secondary_sales.html", form=form)
