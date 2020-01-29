<img width="150" height="150" src="https://cdn2.iconfinder.com/data/icons/time-management-4/500/time-management-business_15-512.png">

# Vinnutimar
> Script that makes tasks working time and adds to google spreadsheet

## Installation
You must have:
* Python

You must have these packages installed:
* gspread
* oauth2client

You can follow a [video tutorial](https://www.youtube.com/watch?v=vISRn5qFrkM), you can follow the steps in the video to 1:48 in the video. Name the credentials json file **client_cred.json**

Create a google sheets document called vinnutimar or change line 16 in spreatsheet_enty.py
```python
sheet = client.open('Your file name').sheet1
```
Final step is to add the *client_email* email from the credinatial json file to working sheet and give it can edit rights.

## How to use it
Simply run the python script with command:
```shell
$ python .\spreatsheet_entry.py
```
It will ask what task you will perform, then the script will run until you exit using **CTRL + C**. It will write to the sheet specified in the code.

### What goes in the sheet
What the script will add to the sheet is a row with `DATE,TIME-START,TIME-END,TIME-SPENT,TASK`
