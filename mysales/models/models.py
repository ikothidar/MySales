from datetime import date

# Local Modules
from mysales.extensions import db


class GSTDetails(db.Model):
    __tablename__ = "gst_details"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    gst_number = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String, nullable=False)
    hsn_code = db.Column(db.String)

    def __repr__(self):
        return f"<GSTDetails {self.name}>"


class PrimarySales(db.Model):
    __tablename__ = "primary_sales"

    entry_date = db.Column(
        db.Date,
        default=lambda: date.today(),
        nullable=False
    )
    gst_number = db.Column(db.String(15), nullable=False)
    party_name = db.Column(db.String, nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    invoice_date = db.Column(db.Date, default=lambda: date.today())
    goods_details = db.Column(db.Text, nullable=False)
    hsn_code = db.Column(db.String, nullable=False)
    total_bill = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    tax_amount = db.Column(db.Float, nullable=False)
    gst_percentage = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            gst_number, invoice_number,
        ),
    )

    def __repr__(self):
        return f"<PrimarySales {self.invoice_number}>"


class SecondarySales(db.Model):
    __tablename__ = "secondary_sales"

    entry_date = db.Column(
        db.Date,
        default=lambda: date.today(),
        nullable=False
    )
    gst_number = db.Column(db.String(15), nullable=False)
    party_name = db.Column(db.String, nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    invoice_date = db.Column(
        db.Date,
        default=lambda: date.today(),
        nullable=False
    )
    goods_details = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    total_bill = db.Column(db.Integer, nullable=False)
    gst_percentage = db.Column(db.Integer, nullable=False)
    tax_amount = db.Column(db.Float, nullable=False)
    cgst = db.Column(db.Float, nullable=False)
    sgst = db.Column(db.Float, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            gst_number, invoice_number,
        ),
    )

    def __repr__(self):
        return f"<SecondarySales {self.invoice_number}>"
