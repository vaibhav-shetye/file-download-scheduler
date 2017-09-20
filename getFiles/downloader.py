import subprocess


class downloader():
    def __init__(self):
        pass

    def download_file(self, user, server, source, destination):
        cmd = 'scp %s@%s:%s %s' %(user, server, source, destination)
        proc = subprocess.Popen(cmd.split())
        return proc.pid
