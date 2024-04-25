from django.shortcuts import render
from subprocess import call
from .models import VirtualMachine
import os
import paramiko
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def ssh_view(request):
    if request.method == 'POST':
        print(2)
        data = json.loads(request.body)
        command = data.get('command')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("doneq!")
        private_key_path = os.path.expanduser('.vagrant/machines/default/virtualbox/private_key')
        ssh.connect('127.0.0.1', username='vagrant', key_filename=private_key_path, port=2222)
        print("doneff")
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        print("done!")

        ssh.close()
        return render(request, 'vms/terminal.html', {'output': output})
    return render(request, 'vms/terminal.html')


def vnc_interface(request):
    return render(request, 'vms/vnc.html')


def home(request):
    return render(request, 'vms/home.html')

def create_vm(request):
    # Call Vagrant to create the virtual machine
    os.environ["VM_HOSTNAME"] = "my-vm-hostname"
    call(['vagrant', 'up'])
    
    # Update the status of the virtual machine
    # vm = VirtualMachine.objects.get(name='MyVM')
    # vm.status = 'Running'
    # vm.save()
    print("dweeeeeeeeee")
    return render(request, 'vms/terminal.html')
