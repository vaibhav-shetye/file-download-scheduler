class scheduler():
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
