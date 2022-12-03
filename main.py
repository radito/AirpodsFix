import sys
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Main Program')

parser.add_argument('--int_out', type=str, help='Interface Out')
parser.add_argument('--int_dmy', type=str, help='Interface Dummy')

args = parser.parse_args()

if args.int_out == None:
    print("Empty Interface Out !")
    sys.exit(0)
    
if args.int_dmy == None:
    print("Empty Interface Dummy !")
    sys.exit(0)

SWITCHER = '/opt/homebrew/bin/SwitchAudioSource'
 
INTERFACE_AIRPODS=args.int_out
INTERFACE_DUMMY=args.int_dmy

TRESHOLD = 10
COUNTER = 0

os.system("echo \"Starting Python Script...\n\"")

for line in sys.stdin:
    COUNTER += 1

    if COUNTER >= TRESHOLD:
        COUNTER = 0

        now = datetime.today().isoformat()

        os.system("echo '[{0}] Airpods Stuttering... ' ".format(now))

        os.system('{0} -t output -s "{1}" && {2} -t output -s "{3}"'.format(SWITCHER, INTERFACE_DUMMY, SWITCHER, INTERFACE_AIRPODS))