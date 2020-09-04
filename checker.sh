#!/bin/bash
echo "SSH keys:"
grep -v "AAAAC3NzaC1lZDI1NTE5AAAAIIWNTYbAStY69IuqJvxMFzpKOrEHH25mpk4Jfnn6BRCV" ~/.ssh/authorized_keys | grep -v "AAAAC3NzaC1lZDI1NTE5AAAAII1nmNT+Dnw8TGsWISPoNo0LlFpflXlfXQCIRgGpWyky" | grep "ssh" && echo "FOUND UNKNOWN SSH AUTHORIZED KEYS!"
echo
echo


echo "Connessioni dagli attaccanti:"
netstat -antp | grep ESTABLISHED | grep -P "10\.0\.\d{1,2}\.\d{1,3}" | grep -Pv "10\.0\.12\.\d{3}"
echo
echo


echo "File modificati meno di mezzora fa in /etc:"
find /etc/ -type f -mmin -30 -ls
echo
echo

echo "File modificati meno di mezzora fa in /root:"
find /root/ -type f -not -path '/root/.local/*' -not -path '/root/.cache/*' -not -path '/root/.config/*' -mmin -30 -ls
echo
echo


echo "File modificati meno di mezzora fa in /home:"
find /home/ -type f -not -path '/home/*/.local/*' -not -path '/home/*/.cache/*' -not -path '/home/*/.config/*' -mmin -30 -ls
echo
echo
