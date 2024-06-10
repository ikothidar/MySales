from enum import Enum

TARGET_LOCATION = r'C:/Users/6129158/Projects/PA/MySales/data/files/'

# Report file valid Headers
PRIMARY_SALES_HEADER = (
    'Entry Date',
    'Name of the party', 
    'GST no of party', 
    'Invoice No', 
    'Invoice Date',
    'Details of Goods',
    'HSN code',
    'GST Percentage',
    'Total amount of bill', 
    'Taxable amount before GST',
    'IGST',
    'CGST',
    'SGST',
)

SECONDARY_SALES_HEADER = (
    'Entry Date',
    'Name of the party', 
    'GST no of party', 
    'Invoice No', 
    'Invoice Date',
    'Details of Goods',
    'Type of Product',
    'GST Percentage',
    'Total Amount of Bill',
    'Taxable Value ',
    'CGST', 
    'SGST',
    'Total GST',
)

# Valid fields for Table
PRIMARY_VALID_FIELDS = [
    'entry_date',
    'gst_number',
    'party_name',
    'invoice_number',
    'invoice_date',
    'goods_details',
    'hsn_code',
    'gst_percentage',
    'total_bill',
    'taxable_value',
    'igst',
    'cgst',
    'sgst',
]

SECONDARY_VALID_FIELDS = [
    'entry_date',
    'gst_number',
    'party_name',
    'invoice_number',
    'invoice_date',
    'goods_details',
    'gst_percentage',
    'taxable_value',
    'total_bill',
    'product_type',
    'tax_amount',
    'cgst',
    'sgst',
]

# Form drop down options
GST_APPLICABILITY = [
    'InterState', 'IntraState',
]

PRODUCT_TYPES = [
    ('Ayurvedic Medicine', 'Ayurvedic Medicine'),
    ('Compression Garments', 'Compression Garments'),
    ('Abdominal Belts', 'Abdominal Belts'),
]


class FetchTypes(Enum):
    PRIMARY_SALES = 'Primary'
    SECONDARY_SALES = 'Secondary'
