import datetime
from utils import ScanResultInsert

class ExpFrameWork:
    def __init__(self, taskid, taskname, vulnid, ipaddress, port, scanfunc):
        self.taskid = taskid
        self.taskname = taskname
        self.vulnid = vulnid
        self.ipaddress = ipaddress
        self.port = port
        self.scanfunc = scanfunc
        self.result = None
        self.date = None

    def execute(self):
        self.result, self.scanlog = self.scanfunc(self.ipaddress, self.port)
        self.date = str(datetime.date.today())
        ScanResultInsert(self.taskid, self.taskname, self.vulnid, self.scanlog, self.result, self.date, self.ipaddress ,self.port)


