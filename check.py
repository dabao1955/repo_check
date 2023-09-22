import os
import subprocess
import sys
from datetime import datetime

try:
    subprocess.call(['python', 'bin/geturl.py'])
    os.system('bash bin/checkurl | grep 301')
    os.system('bash bin/checkurl | grep 404')
    print("# KernelSU repo status")
    print()
    print(f"Updated on {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}")
    print()
    print("| repo url | repo status |")
    print("| -------- | -------- | ")

except:
    sys.exit()
