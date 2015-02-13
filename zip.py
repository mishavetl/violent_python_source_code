import zipfile, sys

###### NOT WORKING PROPERLY USE NORMAL ARCHIVER ######

# TODO:
file = "foo.zip"
password = "secret"
##

zFile = zipfile.ZipFile(file, mode="w")
zFile.writestr("foo.txt", "||foobarbaz test||")
zFile.setpassword(password)

zFile.close()
sys.exit()
