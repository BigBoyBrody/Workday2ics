from openpyxl import workbook
from ics import Calendar, Event

startDates = [
    "A": [2026,8,20],
    "B": [2026,10,19],
    "C": [2027,1,13],
    "D": [2026,3,15],
    "Fall": [2026,8,20],
    "Spring": [2026,1,13]
]
endDates = [
    "A": [2026,10,9],
    "B": [2026,12,11],
    "C": [2027,3,5],
    "D": [2026,5,5],
    "Fall": [2026,8,20],
    "Spring": [2026,5,5]
]

def findLastRowIndex(sheet):
    count = 0
    for x in range(3,100):
        if sheet.cell(x,1).value != None:
            count+=1
        else:
            return count


def parse_wd_excel (filepath):
    c = Calendar()

    wb = workbook.load_workbook(filepath)
    sheet = wb.active
    for x in range(3,findLastRowIndex(sheet)):
        e = Event()
        e.summary = sheet.cell(x,2).value + " - " + sheet.cell(x,3).value
        e.begin


    
    
    



