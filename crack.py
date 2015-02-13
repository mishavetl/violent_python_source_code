#!/usr/bin/python

import subprocess

def testPass(cryptPass, salt):
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = subprocess.check_output(["mkpasswd", "-m", "SHA-512", word, salt]).strip()
        if cryptWord == cryptPass:
            print "[+] Found Password: "+ word + "\n"
            return

    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if "$" in line:
            user = line.split(':')[0]
            salt = line.split('$')[2]
            cryptPass = line.split(':')[1]
            print "[*] Cracking Password For: " + user
            testPass(cryptPass, salt)

if __name__ == "__main__":
    main()
