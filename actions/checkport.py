from st2common.runners.base_action import Action
import socket

class RunCheckPort(Action):
    def run(self, device_ip, port):
        self.check_port(device_ip, port)


    def check_port(self, hostname, port):
        # Create a TCP socket
        s = socket.socket()
        print("Attempting to connect to {} on port {}\n".format(hostname, port))
        try:
            s.connect((hostname, 9001))
            print("Connected to {} on port {}".format(hostname, port))
            s.close()
            return True, "SUCCESS"
        except:
            print("Connection to {} on port {} failed".format(hostname, port))
            return False, 'FAIL'
