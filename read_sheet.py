import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Google Sheets API bağlantısı için yetkilendirme
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = '/Users/aysegul/Documents/GitHub/API_dosya_cekme/sheets-access.json' 

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

client = gspread.authorize(credentials)

# Google Sheets bağlantısı
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1shG9jPQhwYKsPk-CnYAtrZtWG-AkALGeBHgJ0zOTLmc/edit#gid=0"
spreadsheet = client.open_by_url(SPREADSHEET_URL)
worksheet = spreadsheet.sheet1

# Veriyi çek ve pandas DataFrame'e dönüştür
data = worksheet.get_all_records()
df = pd.DataFrame(data)

print(df)

# ROAS hesapla (Revenue / Spend)
df['ROAS'] = df['Revenue (USD)'] / df['Spend (USD)']

# Sonuçları yazdır
print(df[['Channel', 'Campaign', 'Spend (USD)', 'Revenue (USD)', 'ROAS']])