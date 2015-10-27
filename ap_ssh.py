import paramiko
import time


class MyAP:

    def __init__(self, ip):

        self.ip = ip
        self.username = "admin"
        self.password = "admin"

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(self.ip, username = self.username, password = self.password)

    def close(self):
        self.ssh.close()

    def get_countrycode(self):
        stdin, stdout, stderr = self.ssh.exec_command('cat /tmp/system.cfg | grep radio.countrycode')
        tmp_list = stdout.read().split('=')
        print tmp_list[1]
        return int(tmp_list[1])

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        for line in stdout.read().splitlines():
            print line


if __name__ == "__main__":
    ap = MyAP('192.168.1.251')
    ap.connect()
    ap.get_countrycode()


    # fo = open('commands', 'r')
    # for line in fo:
    #     command = line
    #     ap.exec_command(command)
    #     time.sleep(1)









##ssh = paramiko.SSHClient()
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##ssh.connect("192.168.1.218", username='admin', password = 'admin')
##
##stdin, stdout, stderr = ssh.exec_command('iwconfig')
##output = stdout.readlines()
##
##print output
