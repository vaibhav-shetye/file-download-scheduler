import os
import time
from apscheduler.schedulers.background import BackgroundScheduler

#-- Import custom libraries
from getFiles import downloader


if __name__ == '__main__':
    dl = downloader.downloader()
    dl.load_schedule('config/schedule.cfg')

    #-- Create scheduler instance
    scheduler = BackgroundScheduler()

    for start_time in dl.schedule:
        for dl_sch in dl.schedule[start_time]:
            st_time = start_time.split(':')
            print(start_time, ' '.join(dl_sch))
            scheduler.add_job(dl.download_file, 'cron', dl_sch[1:], hour=st_time[0], minute=st_time[1])

    print('-'*80)
    scheduler.print_jobs()
    print('-'*80)

    scheduler.start()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
