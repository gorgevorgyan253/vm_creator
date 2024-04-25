import json
from channels.generic.websocket import WebsocketConsumer
from .utils import SSHClient

class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        if 'command' in data:
            command = data['command']
            ssh_client = SSHClient('your_server_ip', 22, 'your_ssh_username', password='your_ssh_password')
            stdout, stderr = ssh_client.exec_command(command)
            self.send(text_data=json.dumps({'stdout': stdout, 'stderr': stderr}))

