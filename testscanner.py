import subprocess
import os

# COLOUR codes for colourfull output
GREEN = '\033[92m'
FAIL = '\033[91m'
HEADER = '\033[0m'

program_path = "./testscanner"
input_files_path = "./input"

# Functions
def getFileList(dir):
    return [ f for f in os.listdir(dir) ]

def compare(strA, strB):
    linesA = strA.split("\n")
    linesB = strB.split("\n")
    isgood = True
    for index, line in enumerate(linesA):
        if line != linesB[index]:
            print  FAIL + "Error on line " + str(index) + ": " + HEADER + line + FAIL + " must be " + HEADER + linesB[index] 
            isgood = False
    if isgood:
        print GREEN + "Passed" + HEADER

# START
input_files = getFileList(input_files_path)
input_files.sort()

# Call the program and the code to run
for file in input_files:
    p = subprocess.Popen([program_path, os.path.join(input_files_path, file)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print file
    if err != "":
        print FAIL + err + HEADER
    else:
        print GREEN  + out + HEADER

