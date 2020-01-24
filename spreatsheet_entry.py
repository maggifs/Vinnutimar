import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt
import signal, sys

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_cred.json', scope)
client = gspread.authorize(creds)

task = input('Write what task you will perform: ')

# Get start time of task
start = dt.now()#.strftime("%H:%M:%S")

# Open sheets doc
sheet = client.open('vinnutimar').sheet1

# Convert timedelta to Hours:Minutes:Seconds string
def td_converter(tt):
    hours = tt.seconds//3600
    minutes = (tt.seconds//60)%60
    return (str(hours) + ':' + str(minutes) + ':' + str(tt.seconds))

def signal_handler(sig, frame):
    # Get todays date
    date = dt.today().strftime('%d/%m/%Y')

    # Get end time of task
    end = dt.now()#.strftime("%H:%M:%S")

    # Diffrence between end and start time
    tt = end-start
    # convert total time timedelta to string
    tt = td_converter(tt)

    # Row line to add to the spreadsheet
    row_line = [date, start.strftime('%H:%M:%S'), end.strftime('%H:%M:%S'), tt, task]
    # Append line to spreadsheet
    sheet.append_row(row_line)

    print("Row added to spreatsheet:", row_line)
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

while True:
    pass