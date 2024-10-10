'''1.Automated Backup Solution:
    Write a script to automate the backup of a specified directory to a remote
server or a cloud storage solution. The script should provide a report on the
success or failure of the backup operation.'''

import os
import subprocess
import datetime

def backup_directory(local_directory, remote_directory, remote_host, remote_user, ssh_key):
    # Create a timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    # Backup command
    cmd = [
        'rsync', '-avz', '-e', f'ssh -i {ssh_key}',
        local_directory,
        f'{remote_user}@{remote_host}:{remote_directory}_{timestamp}'
    ]
    
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        report = f"Backup successful: {result.stdout}"
        status = "Success"
    except subprocess.CalledProcessError as e:
        report = f"Backup failed: {e.stderr}"
        status = "Failure"
    
    # Save the report
    report_file = os.path.join(local_directory, 'backup_report.txt')
    with open(report_file, 'a') as file:
        file.write(f"{timestamp}: {status}\n{report}\n\n")
    
    print(report)

# Usage
local_directory = '/path/to/local/directory'
remote_directory = '/path/to/remote/directory'
remote_host = 'your.remote.server'
remote_user = 'remote_user'
ssh_key = '/path/to/ssh/key'

backup_directory(local_directory, remote_directory, remote_host, remote_user, ssh_key)