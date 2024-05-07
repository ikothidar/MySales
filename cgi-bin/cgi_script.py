#!c:/Users/6129158/Envs/personal/Scripts/python.exe

print("Content-type:text/html\n\n")

import cgi, cgitb

from config.utils import DATABASE_FILENAME, DBTables
from handlers.primary_sales import PrimarySales
from handlers.secondary_sales import SecondarySales
from handlers.sqlite import SQLite

cgitb.enable(display=0, logdir="./logs")


def main():
    # Get submitted form data.
    form = cgi.FieldStorage()

    form_id = form.getfirst('form_id')

    if form_id == DBTables.PRIMARY_SALES.value:
        data_object = PrimarySales(form=form)
        table_name = DBTables.PRIMARY_SALES.name
    elif form_id == DBTables.SECONDARY_SALES.value:
        data_object = SecondarySales(form=form)
        table_name = DBTables.SECONDARY_SALES.name
    else:
        print('404 Not Found')
        return None
    
    data = data_object.main()

    db = SQLite(filename=DATABASE_FILENAME, table=table_name)

    result = db.insert(row=data)

    if result:
        print(f"Fetched Result from Query: {result}")

    print("Successfully inserted data.")
    

main()
