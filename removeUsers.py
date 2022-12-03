#!/usr/bin/python3
import subprocess,os

subprocess.run(["sudo","apt-get","update"])


expectedUsers = ["adminbee","bigbee","smolbee","swolbee","jimbee","derbee","gabee"] # briefing packet users
users = [] # empty array to hold user names from machine

subprocess.run(["touch","userList.txt"]) # creates textfile "userList.txt"
os.system("awk -F: \'$3 >= 1000 && $1 != \"nobody\" {print $1}\' /etc/passwd > userList.txt") # lists all normal users on the machine and pastes output into "userList.txt"


with open("userList.txt") as file: # inputs each name line by line into the user array
    users = [line.rstrip() for line in file]

for test in users: # if the box has users that are not from expectedUsers, it will delete them
    counter = 7
    for expected in expectedUsers:
            if(test == expected):
                counter = counter - 1
    if (counter == 7):
        subprocess.run(["sudo","userdel","-r",test])
        print("Deleted User: " + test)

subprocess.run(["netstat", "-tulpn"])

subprocess.run(["sudo", "systemctl", "list-units", "--type", "service"])
