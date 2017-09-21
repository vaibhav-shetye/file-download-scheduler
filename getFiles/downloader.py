import subprocess
from datetime import datetime


class downloader():
    def __init__(self):
        self.schedule = dict()


    def load_schedule(self, cfg_file):
        with open(cfg_file, 'r') as cfg:
            for line in cfg:
                col = line.rstrip().split(',')
                start_time = col.pop(0)
                if start_time not in self.schedule:
                    self.schedule[start_time] = list()
                self.schedule[start_time].append(col)


    def download_file(self, user, server, source, destination):
        cmd = 'scp %s@%s:%s %s' %(user, server, source, destination)
        self.print_timestamp(cmd)
        proc = subprocess.Popen(cmd.split())
        return proc.pid


    def print_timestamp(self, msg):
        print('%s : %s' % (datetime.now(), msg))
