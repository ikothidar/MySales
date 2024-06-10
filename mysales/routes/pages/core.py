# Flask modules
from flask import Blueprint, flash, redirect, render_template, url_for
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
            start_date=form_data['start_date'],
            end_date=form_data['end_date']
        )

        return fetch_obj.create_workbook()

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
            int(form_data['taxable_value']) *
            int(form_data['gst_percentage']) / 100, 2
        )
        form_data['total_bill'] = (
            int(form_data['taxable_value']) + round(tax_amount + 0.01, 0)
        )

        if form_data['gst_applicability'] == 'IntraState':
            form_data['igst'] = tax_amount
        elif form_data['gst_applicability'] == 'InterState':
            form_data['cgst'] = tax_amount / 2
            form_data['sgst'] = tax_amount / 2

        for field_name, field_value in form_data.items():
            if field_name in PRIMARY_VALID_FIELDS:
                setattr(primary_obj, field_name, field_value)

        try:
            db.session.add(primary_obj)
            db.session.commit()

            flash(
                f"Data Stored successfully for {primary_obj.invoice_number}",
                "success"
            )
        except Exception as ex:
            flash(
                f"Failed to save invoice: {primary_obj.invoice_number}",
                "error"
            )

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
            int(form_data['taxable_value']) *
            int(form_data['gst_percentage']) / 100, 2
        )
        form_data['tax_amount'] = tax_amount
        form_data['cgst'] = tax_amount / 2
        form_data['sgst'] = tax_amount / 2
        form_data['total_bill'] = (
            int(form_data['taxable_value']) + round(tax_amount + 0.01, 0)
        )

        for field_name, field_value in form_data.items():
            if field_name in SECONDARY_VALID_FIELDS:
                setattr(secondary_obj, field_name, field_value)

        try:
            db.session.add(secondary_obj)
            db.session.commit()

            flash(
                f"Data Stored successfully for {secondary_obj.invoice_number}",
                "success"
            )
        except Exception as ex:
            flash(
                f"Failed to save invoice: {secondary_obj.invoice_number}",
                "error"
            )

    return render_template("pages/secondary_sales.html", form=form)
