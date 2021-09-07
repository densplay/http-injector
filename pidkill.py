import subprocess
import os
def handler():
    print('killing process ...')
    cmd = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    output, error = cmd.communicate()
    target_process = "python"
    for line in output.splitlines():
        if target_process in str(line):
            pid = int(line.split()[0])
            os.system(f'kill {pid} 2> /dev/null')
            os.system(f'pkill screen 2> /dev/null')
            os.system(f'screen -wipe 2> /dev/null')

handler()
