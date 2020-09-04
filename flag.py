#!/usr/bin/python
import requests
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 2:
	print("Usage:", sys.argv[0], "<flag>")
	exit(0)

print("Sending...")
url = 'https://finals.cyberchallenge.it/submit'
team_token = 'mA1wnX9rPXw3hwn1'
stolen_flag = str(sys.argv[1])

r = requests.post(url, data={'team_token': team_token, 'flag': stolen_flag})
if r.status_code == 200:
	print(bcolors.OKGREEN, end='')
else:
	print(bcolors.FAIL, end='')
print(r.status_code, r.reason, bcolors.ENDC)
for line in r.text.splitlines():
	if "flag is invalid" in line or "flag is expired" in line or "Duplicated flag" in line or "token does not match" in line or "flag is your own" in line or "service is corrupted" in line:
		print (bcolors.FAIL, line.strip(), bcolors.ENDC, sep='')
		break
	if "Flag accepted" in line:
		print (bcolors.OKGREEN, line.strip(), bcolors.ENDC, sep='')
		break

