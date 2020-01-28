import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt
import signal, sys, time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_cred.json', scope)
client = gspread.authorize(creds)

task = input('Write what task you will perform: ')

# Get start time of task
start = dt.now()#.strftime("%H:%M:%S")
time.sleep(1)
print('Time is being recording')

# Convert timedelta to Hours:Minutes:Seconds string
def td_converter_hm(tt):
    #hours = tt.seconds//3600
    #minutes = (tt.seconds//60)%60
    hours, remainder = divmod(tt.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (str(hours) + ':' + str(minutes) + ':' + str(seconds))

# Convert timedelta to seconds int
def td_converter_sec(tt):
    seconds = tt.seconds
    return seconds

#checks if token is expired if then refresh and add row
def add_row(row):
  try:
    gs_client = gspread.authorize(creds)
    # Open sheets doc
    gs_worksheet = gs_client.open("vinnutimar").sheet1
    if creds.access_token_expired:
      gs_client.login()  # refreshes the token
    # Append line to spreadsheet
    gs_worksheet.append_row(row)
  except Exception:
    print('error token expired')

def signal_handler(sig, frame):
    # Get todays date
    date = dt.today().strftime('%d/%m/%Y')

    # Get end time of task
    end = dt.now()#.strftime("%H:%M:%S")

    # Diffrence between end and start time
    tts = end-start
    # convert total time timedelta to string
    tt = td_converter_hm(tts)
    #convert total timedelta to seconds int
    tts = td_converter_sec(tts)

    # Row line to add to the spreadsheet
    row_line = [date, start.strftime('%H:%M:%S'), end.strftime('%H:%M:%S'), tt, tts, task]

    # add row to sheets
    add_row(row_line)

    print("Row added to spreatsheet:", row_line)
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

while True:
    pass