#!/usr/bin/python3
import subprocess

expectedUsers = ["kali","bigbee","smolbee","swolbee","jimbee","derbee","gabee"] # briefing packet users
users = [] # empty array to hold user names from box

subprocess.run(["touch","userList.txt"]) # creates textfile "userList.txt"
subprocess.run(["awk","-F:","'$3",">=","1000","&&","$1","!=","nobody","{print $1}'","/etc/passwd"]) # outputs users on machine and copies output into "userList.txt"


with open("userList.txt") as file: # inputs each name line by line into the user array
    users = [line.rstrip() for line in file]

for test in users: # if the box has users that are not from expectedUsers, it will delete them
    counter = 7
    for expected in expectedUsers:
            if(test == expected):
                counter = counter - 1
    if (counter == 7):
        subprocess.run(["sudo","userdel","-r",test])

