from enum import Enum
from typing import Optional

TARGET_LOCATION = r"C:/Users/6129158/Projects/PA/MySales/data/files/"

SALE_TYPE = ['Primary', 'Secondary']

PRIMARY_SALES_HEADER = (
    'Date', 
    'Name of the party', 
    'GST no of party', 
    'Invoice No', 
    'Date', 
    'Details of Goods', 
    'HSN code',
    'Total amount of bill', 
    'Taxable amount before GST', 
    'IGST @12%', 
    'IGST @5%', 
    'CGST @6% and 2.5%',
    'SGST @6% and 2.5%',
)

SECONDARY_SALES_HEADER = (
    'Date', 
    'Name of the party', 
    'GST no of party', 
    'Invoice No', 
    'Date', 
    'Details of Goods',
    'Total Amount of Bill', 
    'Taxable Value @12% Ayurvedic Medicine',
    'Taxable Value @12% Compression Germents', 
    'Taxable Value @5% Abd.Belts', 
    'CGST', 
    'SGST',
    'Total GST',
)

PRIMARY_VALID_FIELDS = [
    'entry_date',
    'gst_number',
    'party_name',
    'invoice_number',
    'invoice_date',
    'goods_details',
    'hsn_code',
    'total_bill',
    'amount',
    'tax_amount',
    'gst_percentage',
]

SECONDARY_VALID_FIELDS = [
    'entry_date',
    'gst_number',
    'party_name',
    'invoice_number',
    'invoice_date',
    'goods_details',
    'amount',
    'total_bill',
    'gst_percentage',
    'tax_amount',
    'cgst',
    'sgst',
]


class FormTypes(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    FETCH_REPORT = 'fetch'


class FetchTypes(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    BOTH_SALES = 'both_sales'
