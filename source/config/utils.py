from enum import Enum
from typing import Optional

DATABASE_FILENAME = (
    r"C:/Users/6129158/Projects/PA/MySales/data/databases/MySales.db"
)

TARGET_LOCATION = r"C:/Users/6129158/Projects/PA/MySales/data/files/"

SALE_TYPE = ['Primary', 'Secondary']

VALID_MONTHS = {
    'jan': '01', 
    'feb': '02', 
    'mar': '03', 
    'apr': '04', 
    'may': '05', 
    'jun': '06', 
    'jul': '07', 
    'aug': '08', 
    'sep': '09', 
    'oct': '10', 
    'nov': '11', 
    'dec': '12',
}

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

SECONDARY_SALES_HEADER= (
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


class DBTables(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    GST_DETAILS = 'gst'


class FormTypes(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    FETCH_REPORT = 'fetch'


class FetchTypes(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    BOTH_SALES = 'both_sales'


def get_name_from_gst(
    gst_number: str,
    hsn_code: Optional[int] = None,
    table_name: Optional[str] = DBTables.GST_DETAILS.name,
) -> str:
    """
    Method to get gst registered name 
    from the given GST Number.

    Args:
        gst_number (str): 
            GST Number to search with.
        hsn_code (int): 
            HSN Code to search with.
        table_name (str): Defaults to DBTables.GST_DETAILS.name.
            table name to fetch data from.

    Returns:
        str: vendor name fetched using gst number. 
    """
    db = SQLite(filename=DATABASE_FILENAME, table=table_name)

    condition = f"WHERE GST_NUMBER = '{gst_number}'"
    
    if hsn_code:
        condition += f"{condition} AND HSN_CODE = '{hsn_code}'"

    result = list(
        db.get_data(columns=['NAME'], condition=condition, limit=1)
    )

    if not result:
        return None
    
    return result[0]
