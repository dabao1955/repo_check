import os
import subprocess
import sys
try:
    subprocess.call(['python', 'bin/geturl.py'])
    os.system('bash bin/checkurl | grep 301')
    print()
    os.system('bash bin/checkurl | grep 404')
except:
    sys.exit()
