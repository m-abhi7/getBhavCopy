import io
import zipfile
import requests
import pandas as pd

from datetime import date, timedelta

#get today's date
today = date.today()

#convert it into the format DDMMMYYYY
formatted_date = today.strftime("%d%b%Y").upper()

print("Fetching bhav copy for the date:", formatted_date)

#create filename with the format cmDDMMMYYYYbhav.csv, which will be later used in the url and while extracting
filename = "cm" + formatted_date + "bhav.csv"

#generate url for today's file
url = "https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/{filename}.zip".format(year = today.year, month = today.strftime("%b").upper(), filename = filename)
response = requests.get(url)

#convert contents of response into bytes 
bytesContent = io.BytesIO(response.content)

#load bytes object into a zip file
with zipfile.ZipFile(bytesContent, 'r') as zip_ref:
    #unzip contents of file into memory
    csvFile = zip_ref.read(filename)

#convert unzipped csv file into a pandas dataframe
bhavcopy = pd.read_csv(io.BytesIO(csvFile))
print(bhavcopy)