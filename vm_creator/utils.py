import paramiko

class SSHClient:
    def __init__(self, host, port, username, password=None, key_filename=None):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if password:
            self.client.connect(host, port, username, password)
        else:
            self.client.connect(host, port, username, key_filename=key_filename)

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        self.client.close()
