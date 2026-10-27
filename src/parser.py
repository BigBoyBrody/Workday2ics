from openpyxl import workbook
from ics import Calendar, Event
from datetime import datetime, timezone, timedelta


startDates = {
    "A": [2026,8,20],
    "B": [2026,10,19],
    "C": [2027,1,13],#todo get a way by asking or fetching 
    "D": [2026,3,15],
    "Fall": [2026,8,20],
    "Spring": [2026,1,13]
}
endDates = {
    "A": [2026,10,9],
    "B": [2026,12,11],
    "C": [2027,3,5],
    "D": [2026,5,5],
    "Fall": [2026,8,20],
    "Spring": [2026,5,5]
}

def findLastRowIndex(sheet):
    count = 0
    for x in range(3,100):
        if sheet.cell(x,1).value != None:
            count+=1
        else:
            return count

def getStartDate(startPeriod):
    for x in len(startDates):
        if startPeriod.find(list(startDates)[x]) != -1:
            return startDates[x]
    return -1

def getStartTime(meetingPeriod):
    meetingPeriod = meetingPeriod.split("|")[1] # gets i.e "2:00 PM - 2:50 PM"
    meetingPeriod = (meetingPeriod.split("-")[0]).lstrip() # gets i.e "2:00 PM"
    return [meetingPeriod[0], meetingPeriod[2]]

def parse_wd_excel (filepath):
    c = Calendar()

    wb = workbook.load_workbook(filepath)
    sheet = wb.active
    for x in range(3,findLastRowIndex(sheet)):
        e = Event()
        e.summary = sheet.cell(x,2).value + " - " + sheet.cell(x,3).value
        start = getStartDate(sheet.cell(x,1))
        startTime = getStartTime(sheet.cell(x,1))
        e.begin = datetime(start[0],start[1],start[2])


    
    
    



