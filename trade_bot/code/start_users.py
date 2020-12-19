import sys
import os

def get_command_and_exec(line, fd):
    while line != "":
        if line.find("account_name") != -1:
            name = line[15:len(line)]
        elif line.find("api_url") != -1:
            api_url = line[10:len(line)]
        elif line.find("api_key") != -1:
            api_key = line[10:len(line)]
        elif line.find("api_secret_key") != -1:
            api_secret_key = line[17:len(line)]
        elif line.find("api_passphrase") != -1:
            api_passphrase = line[17:len(line)]
            break
        line = line = fd.readline()
    shell_command = "python2.7 user.py " + name.strip("\n") + " " + api_url.strip("\n") + " " + api_key.strip("\n") + " " + api_secret_key.strip("\n") + " " + api_passphrase.strip("\n")
    os.system(shell_command)


def find_user(line, fd):
    EOF = 0
    while EOF != 2:
        if line.find("account_name") != -1:
            name = line[15:len(line)]
            if name.strip("\n") == sys.argv[1]:
                break
        line = fd.readline()
        if line == "":
            EOF += 1
        else:
            EOF -= 1
    if EOF == 2:
        return False
    else:
        return line

if __name__ == "__main__":
    with open("../users_data/users.txt", "r") as fd:
        line = line = fd.readline()
        line = find_user(line, fd)
        if line == False:
            print("User not found")
            exit()
        get_command_and_exec(line, fd)
