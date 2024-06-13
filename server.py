# import pandas as pd

from mysales import create_app
# from mysales.extensions import db
# from mysales.models.models import GSTDetails

# Dev Environment
# app = create_app(debug=True)

# Prod Environment
app = create_app()


# def populate_gst_data():
#     data = pd.read_csv("data/files/gst_details.csv")
#
#     print(data.keys())
#
#     count = 0
#     for index, row in data.iterrows():
#         new_data = GSTDetails(
#             gst_number=row['GST_NUMBER'],
#             name=row['GST_NUMBER'],
#             hsn_code=row['HSN_CODE']
#         )
#         print(f"my count {count}")
#         db.session.add(new_data)
#     db.session.commit()


if __name__ == '__main__':
    # populate_gst_data()
    app.run()
