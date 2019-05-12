from st2common.runners.base_action import Action
import socket

class RunCheckPort(Action):
    def run(self, device_ip):
        self.check_port(device_ip)


    def check_port(self, hostname):
        # Create a TCP socket
        port = '80'
        s = socket.socket()
        print("Attempting to connect to {} on port {}".format(hostname, port))
        try:
            s.settimeout(self.tcp_session)
            s.connect((hostname, port))
            print("Connected to {} on port {}".format(hostname, port))
            s.close()
            return True, "SUCCESS"
        except:
            print("Connection to {} on port %s failed".format(hostname, port))
            return False, 'FAIL'
