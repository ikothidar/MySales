from cgi import FieldStorage
from datetime import datetime
from .handler_helper import DBTables, get_name_from_gst

TABLE_NAME = DBTables.SECONDARY_SALES.name

class SecondarySales:

    def __init__(self, form: FieldStorage):
        self._form = form

    def generate_query(self, data: dict) -> dict:
        data['entry_date'] = datetime.now().strftime("%Y-%m-%d")

        gst_number = data.get('gst_number')

        if gst_number:
            data['party_name'] = get_name_from_gst(gst_number=gst_number)
        else:
            data['gst_number'] = 'CASH INVOICE'

        tax_amount = round(
            int(data['amount']) * int(data['gst_percentage']) / 100, 2
        )

        data['tax_amount'] = tax_amount
        data['cgst'] = tax_amount / 2
        data['sgst'] = tax_amount / 2
        data['total_bill'] = int(data['amount']) + round(tax_amount + 0.01, 0)

        return data

    
    def main(self):
        data = dict()

        # Getting data from form object
        data['gst_number'] = self._form.getfirst('gst_number')
        data['party_name'] = self._form.getfirst('party_name')
        data['invoice_number'] = self._form.getfirst('invoice_number')
        data['invoice_date'] = self._form.getfirst('invoice_date')
        data['goods_details'] = self._form.getfirst('goods_details')
        data['amount'] = self._form.getfirst('amount')
        data['gst_percentage'] = self._form.getfirst('gst_percentage')

        return self.generate_query(data=data)
    