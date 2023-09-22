import os
import subprocess
import sys
from datetime import datetime

try:
    print("# KernelSU repo status")
    print()
    print(f"Updated on {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}")
    print()
    print("| repo url | repo status |")
    subprocess.call(['python', 'bin/geturl.py'])
    os.system('bash bin/checkurl | grep 301')
    print()
    os.system('bash bin/checkurl | grep 404')
except:
    sys.exit()
