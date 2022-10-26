from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# initializing google sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'
sheet = None
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = '1BFb1NLSb8GAkrWeXv8tKkRvndL5S3abA3xikBcZ5YQk'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# returns a list of values at the given range in the spreadsheet (values represented as strings)
def read(range):
    # gets values with format [['first value'], ['second value']]
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute().get('values')
    
    # reformats data to ['first value', 'second value']
    resultFormatted = []
    for i in result:
        resultFormatted.append(i[0])
    return resultFormatted

# writes a single value to a range
def write(range, value):
    valueRangeBody = {
        'majorDimension': 'ROWS',
        'values': [[value]]
    }
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption='USER_ENTERED', body=valueRangeBody).execute()

def main():
    pass


if __name__ == "__main__":
    main()