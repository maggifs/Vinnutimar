import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt
import signal, sys, time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_cred.json', scope)
client = gspread.authorize(creds)

def tt_converter(ts):
    hours, remainder = divmod(ts, 3600)
    minutes, seconds = divmod(remainder, 60)
    return ("'" + str(hours) + ':' + str(minutes) + ':' + str(seconds))

gs_worksheet = client.open("vinnutimar").sheet1

# Get total seconds value to int
ts = int(gs_worksheet.acell('J2').value)
# Convert total seconds to hour:minute:seconds format
ts = tt_converter(ts)
# Update the total time cell
gs_worksheet.update_acell('J3', ts)

print('Total time has been updated to', ts)