from typing import Optional

from cgi import FieldStorage
from datetime import datetime
from source.config.utils import DBTables, get_name_from_gst

TABLE_NAME = DBTables.PRIMARY_SALES.name


class PrimarySales:

    def __init__(
        self,
        form: Optional[FieldStorage] = None,
    ) -> None:
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
        data['total_bill'] = int(data['amount']) + round(tax_amount + 0.01, 0)

        return data

    def main(self) -> dict:
        data = dict()

        if not self._form:
            return {'error': 'Some error occured while collecting form data'}

        # Getting data from form object
        data['gst_number'] = self._form.getfirst('gst_number')
        data['invoice_number'] = self._form.getfirst('invoice_number')
        data['invoice_date'] = self._form.getfirst('invoice_date')
        data['goods_details'] = self._form.getfirst('goods_details')
        data['hsn_code'] = self._form.getfirst('hsn_code')
        data['amount'] = self._form.getfirst('amount')
        data['gst_percentage'] = self._form.getfirst('gst_percentage')

        return self.generate_query(data=data)
