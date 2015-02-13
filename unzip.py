#!/usr/bin/python

import zipfile
from stem.util import term

# TODO:
file = "some.zip"
dict = "dictionary.txt"
##

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except RuntimeError:
        return False
def main(file):
    valid = 0
    invalid = 0

    words = 0

    for word in open("dictionary.txt", 'r+').read().split():
        words += 1

    zFile = zipfile.ZipFile(file)
    print term.format("\nStarting cracking\n", term.Attr.BOLD)
    passFile = open(dict)
    print term.format("Oppened dictionary with {0} words\n".format(words), term.Color.BLUE)
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess != False:
            print term.format("[+] Password = {0}".format(password), term.Color.GREEN)
            valid += 1
            break
        else:
            print term.format("[-] Password {0} is invalid".format(password), term.Color.RED)
            invalid += 1

    zFile.close()
    passFile.close()
    print term.format("\nPasswords valid: {0} invalid: {1}".format(valid, invalid), term.Color.BLUE)
    print term.format("\nStopping cracking\n", term.Attr.BOLD)
    exit(0)


if __name__ == '__main__':
    main(file)
