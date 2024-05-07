from enum import Enum
from typing import Optional
from .config_helper import SQLite

DATABASE_FILENAME = (
    r"C:/Users/6129158/Projects/PA/Nareshanjali Enterprises/MySales/data/databases/MySales.db"
)
SALE_TYPE = ['Primary', 'Secondary']

class DBTables(Enum):
    PRIMARY_SALES = 'primary'
    SECONDARY_SALES = 'secondary'
    GST_DETAILS = 'gst'


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

    result = list(db.get_data(columns=['NAME'], condition=condition))

    if not result:
        return None
    
    return result[0]
