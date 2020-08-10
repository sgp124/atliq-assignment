import pandas as pd
import db

data_directory = "data/"
file_extention = ".xlsx"

def ingest_vendor_transaction():
	df = pd.read_excel(data_directory+"Vendor Transactions"+file_extention)
	df.columns = ['date','cost','imei','phone','sales_type']
	df['cost'] = df['cost'].str.replace('Rs.', '')
	df['cost'] = df['cost'].str.replace(' ', '')
	df.to_sql('vendor_transactions',db.engine,if_exists = 'replace',index_label='id')


def ingest_vendor_sales_types():
	df = pd.read_excel(data_directory+"Vendor Sales Type"+file_extention)
	df.columns = ['code','sales_type']
	df.to_sql('vendor_sales_types',db.engine,if_exists = 'replace',index_label='id')


def ingest_store_master():
	df = pd.read_excel(data_directory+"Store Master"+file_extention)
	df.columns = ['code','store','city','state']
	df.to_sql('store_master',db.engine,if_exists = 'replace',index_label='id')


def ingest_company_transcation():
	df = pd.read_excel(data_directory+"Company Trans"+file_extention)
	df.columns = ['store','date','trans_id','coustmer_id','imei','phone','trans_type','state']
	df.to_sql('company_transcation',db.engine,if_exists = 'replace',index_label='id')

if __name__ == "__main__":
	print("Ingestion Process Started")
	ingest_vendor_transaction()
	ingest_vendor_sales_types()
	ingest_store_master()
	ingest_company_transcation()