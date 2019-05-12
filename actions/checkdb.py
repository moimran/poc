from st2common.runners.base_action import Action
import mysql.connector

class RunCheckPort(Action):
    def run(self, device_ip, port, db_username, db_password):
        print("Attempting to connect to {} on port {}\n".format(device_ip, port))
        if(self.check_db(device_ip, port, db_username, db_password) == True):
            return True
        else:
            return (False, "Failed!")


    def check_db(self, device_ip, port, db_username, db_password):
        try:
            mydb = mysql.connector.connect(
            host=device_ip,
            port=port,
            user=db_username,
            passwd=db_password,
            auth_plugin="mysql_native_password")
            print("Connection to {} on port {} successful".format(device_ip, port))
            return True
        except:
            print("Connection to {} on port {} failed".format(device_ip, port))
            return False



