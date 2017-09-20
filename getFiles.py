from getFiles import scheduler
from getFiles import downloader

if __name__ == '__main__':
    sch = scheduler.scheduler()
    sch.load_schedule('config/schedule.cfg')
    print(sch.schedule)

    dl = downloader.downloader()
    for start_time in sch.schedule:
        for dl_file in sch.schedule[start_time]:
            user = dl_file[1]
            server = dl_file[2]
            src = dl_file[3]
            dest = dl_file[4]
            pid = dl.download_file(user, server, src, dest)
            print(pid)
