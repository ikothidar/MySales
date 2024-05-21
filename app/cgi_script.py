#!c:/Users/6129158/Envs/personal/Scripts/python.exe

import cgi
import cgitb

from app.config import DATABASE_FILENAME, DBTables, FormTypes
from handlers.fetch_data import FetchData
from handlers.primary_sales import PrimarySales
from handlers.secondary_sales import SecondarySales
from handlers.sqlite import SQLite

print("Content-type:text/pages\n\n")
cgitb.enable(display=0, logdir="./logs")


def main():
    # Get submitted form data.
    form = cgi.FieldStorage()

    form_id = form.getfirst('form_id')

    if form_id == FormTypes.PRIMARY_SALES.value:
        data_object = PrimarySales(form=form)
        table_name = DBTables.PRIMARY_SALES.name
    elif form_id == FormTypes.SECONDARY_SALES.value:
        data_object = SecondarySales(form=form)
        table_name = DBTables.SECONDARY_SALES.name
    elif form_id == FormTypes.FETCH_REPORT.value:
        FetchData(form=form)
        return None
    else:
        print('404 Page Not Found')
        return None
    
    data = data_object.main()

    db = SQLite(filename=DATABASE_FILENAME, table=table_name)

    result = db.insert(row=data)

    if result:
        print(f"Fetched Result from Query: {result}")

    print("Successfully inserted data.")
    

main()
