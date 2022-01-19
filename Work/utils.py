import os
import uuid
import threading
from Work.models import Work
from ExpManager.models import ExpManager

class Scan(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self, name=uuid.uuid1())
        self.id = id
    def run(self):
        taskname = Work.objects.filter(id=self.id).values_list("name")[0][0]
        expid = Work.objects.filter(id=self.id).values_list("exp_id")[0][0]
        vulnid = ExpManager.objects.filter(id=expid).values_list("vulnid")[0][0]
        ipaddress = Work.objects.filter(id=self.id).values_list("ipdst")[0][0]
        path = ExpManager.objects.filter(id=expid).values_list("fileobj")[0][0]
        filepath = str(os.getcwd()) + "/" + str(path)
        port = Work.objects.filter(id=self.id).values_list("port")[0][0]
        command_string = ExpManager.objects.filter(id=expid).values_list("command")[0][0]
        command = command_string % (str(filepath), str(self.id), str(taskname), str(vulnid), str(ipaddress), str(port))
        os.system(command)

