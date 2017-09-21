import subprocess
from datetime import datetime


class downloader():
    def __init__(self):
        self.schedule = dict()


    def schedule_jobs(self, cfg_file, scheduler):
        with open(cfg_file, 'r') as cfg:
            for line in cfg:
                dl_sch = line.rstrip().split(',')
                st_time = dl_sch[0].split(':')
                print(' '.join(dl_sch))
                scheduler.add_job(self.download_file, 'cron', dl_sch[2:], hour=st_time[0], minute=st_time[1])
                '''
                start_time = col.pop(0)
                if start_time not in self.schedule:
                    self.schedule[start_time] = list()
                self.schedule[start_time].append(col)
                '''


    def download_file(self, user, server, source, destination):
        cmd = 'scp %s@%s:%s %s' %(user, server, source, destination)
        self.print_timestamp(cmd)
        proc = subprocess.Popen(cmd.split())
        return proc.pid


    def print_timestamp(self, msg):
        print('%s : %s' % (datetime.now(), msg))
