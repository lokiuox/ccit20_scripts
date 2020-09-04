#!/usr/bin/python
import requests
import sys
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

teams = json.load(open("teams.json", "r"))
ips = {value: key for key, value in teams.items()}

FLAG_ID_URL = "https://finals.cyberchallenge.it/api/flag_id"
SCOREBOARD_URL = "https://finals.cyberchallenge.it/ctf_scoreboard"

def check_valid_id():
	r = requests.get(FLAG_ID_URL)
	if r.status_code != 200:
		print(bcolors.WARNING + "Something went wrong. Code:", r.status_code, r.reason + bcolors.ENDC)
		return
	data = json.loads(r.text)
	return data

def print_flag_id(data, service=None):
	if service is not None:
		if service not in data.keys():
			print(bcolors.FAIL + "No service with this name:", service + bcolors.ENDC)
			return
		print(bcolors.WARNING + service + bcolors.ENDC)
		for host in data[service].keys():
			print(bcolors.OKGREEN + host + " (" + ips[host] + ") :" + bcolors.ENDC)
			for id in data[service][host]:
				print(bcolors.BOLD + key_id + bcolors.ENDC)
	else:
		for service in data.keys():
			print(bcolors.WARNING + service + bcolors.ENDC)
			for host in data[service].keys():
				print(bcolors.OKGREEN + host + " (" + ips[host] + ") :" + bcolors.ENDC)
				for id in data[service][host]:
					print(bcolors.BOLD + key_id + bcolors.ENDC)


def check_status():
	r = requests.get(SCOREBOARD_URL)
	if r.status_code != 200:
		print(bcolors.WARNING + "Something went wrong. Code:", r.status_code, r.reason + bcolors.ENDC)
		return
	data = json.loads(r.text)
	return data

def print_status(data, teams=["uniba"]):
	for team in data["scores"]:
		if team["name"] in teams:
			namefmt = '{:<32} {:<10} {:<10} {:<12} {:<12} {:<12} {:<6}'
			print(namefmt.format(bcolors.BOLD + bcolors.UNDERLINE + "Team " + team["name"] + bcolors.ENDC, "SCORE:", team["score"], "ATTACK:", team["attack"], "DEFENSE:", str(team["defense"]) + bcolors.ENDC))
			fmt1 = '{:<24} {:<31}'
			fmt2 = '{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<6}'
			for servicename, service in team["services"].items():
				#print(bcolors.BOLD + servicename + ": " + "\t\t", end = '')
				if "integrity" in service and "status" in service["integrity"]:
					if service["integrity"]["status"]:
						#print(bcolors.OKGREEN + "ONLINE" + bcolors.ENDC + bcolors.ENDC)
						#print(fmt.format(bcolors.BOLD + servicename + ": ", bcolors.OKGREEN + "ONLINE" + bcolors.ENDC, "ATTACK:", service["attack"], "ATKFLAGS:", service["attack_flags"], "DEFENSE:", service["defense"], "DEFFLAGS:", service["defense_flags"]))
						print(fmt1.format(bcolors.BOLD + servicename + ": ", bcolors.OKGREEN + "ONLINE" + bcolors.ENDC), end='')
					else:
						#print(bcolors.FAIL + "CORRUPTED" + bcolors.ENDC + bcolors.ENDC)
						print(fmt1.format(bcolors.BOLD + servicename + ": ", bcolors.FAIL + "CORRUPTED" + bcolors.ENDC), end='')
						#print(fmt.format(bcolors.BOLD + servicename + ": ", bcolors.FAIL + "CORRUPTED" + bcolors.ENDC, "ATTACK:", service["attack"], "DEFENSE:", service["defense"]))
				else:
					#print(fmt.format(bcolors.BOLD + servicename + ": ", bcolors.WARNING + "NOT CHECKED" + bcolors.ENDC, "ATTACK:", service["attack"], "DEFENSE:", service["defense"]))
					print(fmt1.format(bcolors.BOLD + servicename + ": ", bcolors.WARNING + "NOT CHECKED" + bcolors.ENDC), end='')
					#print(bcolors.WARNING + "NOT CHECKED" + bcolors.ENDC + bcolors.ENDC)
				print(fmt2.format("ATTACK:", service["attack"], "ATKFLAGS:", service["attack_flags"], "DEFENSE:", service["defense"], "DEFFLAGS:", service["defense_flags"]))

print_status(check_status(), "uniba")
print_flag_id(check_valid_id())
