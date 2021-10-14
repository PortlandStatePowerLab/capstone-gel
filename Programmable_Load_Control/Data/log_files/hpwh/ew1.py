import time
import os

while True:
    cmd = os.system("ssh pi@10.200.89.63")
    if cmd==0:
        break
    else:
        os.system('ssh pi@10.200.89.63')
    time.sleep(20)
