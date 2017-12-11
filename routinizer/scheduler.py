import schedule
import time
from executor import executeRoutine, init, getReadIndex, incrementIndex
from datetime import date


def scheduleDaily():
    init()
    schedule.every().day.at("9:00").do(executeRoutine)

    while True:
        schedule.run_pending()
        time.sleep(1)

def scheduleNow():
    executeRoutine()
    incrementIndex()
    scheduleDaily()

def job():
    todayDate = date.today()
    _, lastReadDate = getReadIndex()
    if lastReadDate is None or lastReadDate < todayDate:
        scheduleNow()
    else:
        scheduleDaily()

job()
