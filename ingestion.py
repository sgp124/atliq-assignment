import pandas as pd
import db

data_directory = "data/"
file_extention = ".xlsx"

def ingest_vendor_transaction():
	df = pd.read_excel(data_directory+"Vendor Transactions"+file_extention)
	df.columns = ['date','cost','imei','phone','sales_type']
	print(df)

	df.to_sql('vendor_transactions',db.engine,if_exists = 'append',index_label='id')

if __name__ == "__main__":
	ingest_vendor_transaction()