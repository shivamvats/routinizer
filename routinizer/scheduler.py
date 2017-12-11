import schedule
import time
from executor import executeRoutine, init


def main():
    init()
    schedule.every().day.at("10:18").do(executeRoutine)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
