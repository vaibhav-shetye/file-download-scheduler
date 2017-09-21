import os
import time
from apscheduler.schedulers.background import BackgroundScheduler

#-- Import custom libraries
from getFiles import downloader


if __name__ == '__main__':
    #-- Create scheduler instance
    scheduler = BackgroundScheduler()

    dl = downloader.downloader()
    dl.schedule_jobs('config/schedule.cfg', scheduler)

    print('-'*80)
    scheduler.print_jobs()
    print('-'*80)

    #-- Start the scheduler
    scheduler.start()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
