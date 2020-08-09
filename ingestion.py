import pandas as pd

data_directory = "data/"
file_extention = ".xlsx"

def start_ingestion():
	print("ingestion started")
	df = pd.read_excel(data_directory+"Vendor Transactions"+file_extention)
	print(df)
	

if __name__ == "__main__":
	start_ingestion()