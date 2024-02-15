#WebDataScraper
#A Python3 program by Phil van der Linden.
#This program takes a URL as input, then scrapes the URL and it's HTML code for sensitive data.

#----IMPORT REQUIRED LIBRARIES----

#Import the library for interpreting Bash commands.
import subprocess
#Import the library for regular expression pattern matching.
import re
#Import the libarary for matching Unix-style pathname patterns.
import glob
#Import the library for interacting with the OS.
import os

#----DEFINE GLOBAL VARIABLES----

global interestingList
interestingList = []

global resultsFile
resultsFile = open("search_results.txt", "w")

#----DEFINE FUNCTIONS----

#Function to find all downloaded files in the current directory (tempDir), store them in an array, and then merge them into temp.txt output file.
def files2temp():
        pageArray = []
        for file in glob.glob("*"):
                if not file.startswith('WebDataScraper.py') and not file.startswith('temp.txt'):
                        pageArray.append(file)
        my_cmd = ['cat'] + pageArray
        with open('temp.txt', "w") as outfile:
                subprocess.run(my_cmd, stdout=outfile)

#Note for some of the following functions...
#HTML from WGET often contains strings with a less than or greater than symbols for HTML tags...
#This means strings may be delimited with '<' or '>' rather than \n or \s in many cases.

#Function to search the target file for email addresses.
def search4email():
        print("Possible Emails:")
        resultsFile.write("Possible Emails:\n")
        targetFile = open("temp.txt","r")
        for line in targetFile:
                email = re.search(r'[\w.-]+@[\w.-]+', line)
                if email:
                        print(email.group().replace('<','').replace('>','').replace(' ','').replace('\n',''))
                        resultsFile.write(email.group().replace('<','').replace('>','').replace(' ','').replace('\n','') + "\n")
        targetFile.close()

#Function to search the target file for phone numbers.
def search4phone():
        print("\nPossible Phone Numbers:")
        resultsFile.write("\nPossible Phone Numbers:\n")
        targetFile = open("temp.txt","r")
        for line in targetFile:
                phoneType1 = re.search(r'([>\n\s]{1}\d\d\d[.-]+\d\d\d[.-]+\d\d\d\d[\s\n<]{1})', line)
                if phoneType1:
                        print(phoneType1.group().replace('<','').replace('>','').replace(' ','').replace('\n',''))
                        resultsFile.write(phoneType1.group().replace('<','').replace('>','').replace('\n','') + "\n")
                phoneType2 = re.search(r'([>\n\s]{1}\(+\d\d\d+\)+\s\d\d\d+([ .-]{0,1})+\d\d\d\d[\s\n<]{1})', line)
                if phoneType2:
                        print(phoneType2.group().replace('<','').replace('>','').replace('\n',''))
                        resultsFile.write(phoneType2.group().replace('<','').replace('>','').replace('\n','') + "\n")
        targetFile.close()

#Function to search the target file for social security numbers.
def search4social():
        print("\nPossible Social Security Numbers:")
        resultsFile.write("\nPossible Social Security Numbers:\n")
        targetFile = open("temp.txt", "r")
        for line in targetFile:
                ssn = re.search(r'([>\n\s]{1}\d{3}[-]+\d{2}[-]+\d{4}[\s\n<]{1})', line)
                if ssn:
                        print(ssn.group().replace('<','').replace('>','').replace(' ','').replace('\n',''))
                        resultsFile.write(ssn.group().replace('<','').replace('>','').replace(' ','').replace('\n','') + "\n")
        targetFile.close()

#Function to search the target file for credit card numbers.
def search4cc():
        print("\nPossible Credit Card Numbers:")
        resultsFile.write("\nPossible Credit Card Numbers:\n")
        targetFile = open("temp.txt", "r")
        for line in targetFile:
                ccnType1 = re.search(r'([>\n\s]{1}\d{4}\s\d{4}\s\d{4}\s\d{4}[\s\n<]{1})', line)
                if ccnType1:
                        print(ccnType1.group().replace('<','').replace('>',''))
                        resultsFile.write(ccnType1.group().replace('<','').replace('>','').replace('\n','') + "\n")
                ccnType2 = re.search(r'([>\n\s]{1}\d{4}[-]\d{4}[-]\d{4}[-]\d{4}[\s\n<]{1})', line)
                if ccnType2:
                        print(ccnType2.group().replace('<','').replace('>','').replace(' ','').replace('\n',''))
                        resultsFile.write(ccnType2.group().replace('<','').replace('>','').replace('\n','') + "\n")
        targetFile.close()

#Function to search the target file for interesting strings.
def search4interesting():
        interestingStrings = False
        resultsFile.write("\nInteresting Strings Detected:\n")

        targetFile = open("temp.txt","r")
        for line in targetFile:
                check1 = re.search(r'api=', line)
                if check1:
                        interestingList.append("api=")
                        break
        targetFile = open("temp.txt","r")
        for line in targetFile:
                check2 = re.search(r'token=', line)
                if check2:
                        interestingList.append("token=")
                        break
        targetFile = open("temp.txt","r")
        for line in targetFile:
                check3 = re.search(r'session=', line)
                if check3:
                        interestingList.append("session=")
                        break
        targetFile = open("temp.txt","r")
        for line in targetFile:
                check4 = re.search(r'sessionid=', line)
                if check4:
                        interestingList.append("sessionid=")
                        break
        targetFile = open("temp.txt","r")
        for line in targetFile:
                check5 = re.search(r'userid=', line)
                if check5:
                        interestingList.append("userid=")
                        break
        targetFile = open("temp.txt","r")
        for line in targetFile:
                check6 = re.search(r'cookie=', line)
                if check6:
                        interestingList.append("cookie=")
                        break

        #Check whether interesting strings were found.
        if len(interestingList) > 0:
                interestingStrings = True

        #If interesting strings were found, provide option to list items.
        if interestingStrings == True:
                print("\nInteresting code strings were detected.")
                proceed = input("\nPress \'y\' to view or \'n\' to exit:")
                if proceed == 'y':
                        print("\nOne or more instances of...")
                        for x in range(len(interestingList)):
                                print(interestingList[x])
        targetFile.close()

#----PROGRAM STARTS HERE----

print()
print("|-------------------------------|")
print("|   Running WebDataScraper...   |")
print("|-------------------------------|")
print()
date_cmd = ['date']
print("Started at...")
subprocess.run(date_cmd)
print()

#Have user select a query type.
print("Query Options...")
print("1 - Page Query")
print("2 - Directory Query")
print("3 - Full website Query")
#print("\nFile Options...")
#print("4 - Download PDFs from directory")
#print("5 - Download .doc and .docx from directory")

queryType = input("\nSpecify query type: ")
if queryType == '':
        print("Empty option parameter. Exiting.")
        proc4 = subprocess.run(["rm", "search_results.txt"])
        quit()

#Prompt user for a target, and store the value.
webpage = input("\nEnter target URL: ")
if webpage == '':
        print("Empty target parameter. Exiting.")
        proc4 = subprocess.run(["rm", "search_results.txt"])
        quit()

#Note the starting directory for later, make a temp directory, and move program to the new dir>
initial_cwd = os.getcwd()
proc1 = subprocess.run(["mkdir", "tempDir"])
os.chdir('tempDir')

#Select WGET (plus parameters), based on selected query option.
print("\nAnalyzing files...")
if queryType == '1':
        proc2 = subprocess.run(["wget", "-q", "-np", "--show-progress", webpage])
if queryType =='2':
        proc2 = subprocess.run(["wget", "-q", "-np", "-nd", "--show-progress", "-r", "-l 1", webpage])
if queryType =='3':
        print("** Warning **")
        proceed = input("A full website query is quite noisy and may take a long time. Press 'y' to continue: ")
        if proceed == 'y':
                proc2 = subprocess.run(["wget", "-q", "--show-progress", webpage])
        else:
                proc3 = subprocess.run(["rm","-r", "tempDir"])
                proc4 = subprocess.run(["rm", "search_results.txt"])
                quit()

#WGET Quick Reference:
# -q = Turn off output.
# -S = Include server response headers.
# -np = No parents directories.
# -nd = Prevents new directories from being created.
# -r = Resursively pull files from directories.
# -R = Reject... Set a list for rejected file types, like .txt, .xml, etc.
# -A = Accept... Sets a list for accepted file types, like .html, .pdf, etc.
# -l 1 = Sets the recusion depth to one, when the '-r' tag is present.
# --show-progress = Displays a download progress bar.
# Example WGET commands...
#  wget -nd -r -l 1 -np https://www.google.com
# wget -q --show-progress -A "*.mp3" https://www.example.com

files2temp()

#Setup header for Search_Results.txt.
resultsFile.write("+++++ WebDataScraper Results +++++\n\n")
resultsFile.write("Target: " + webpage + "\n\n")

#----BEGIN STRING SEARCHING----

print()
search4email()
search4phone()
search4social()
search4cc()
search4interesting()

#Return to the program to the original directory.
os.chdir(initial_cwd)

#----SAVING RESULTS----

print("\nWould you like to save these results?")
saveResults = False
proceed = input("\nPress \'y\' to save or \'n\' to exit:")
if proceed == 'y':
        saveResults = True
        saveName = webpage + "_results"
#       resultsFile = open("search_results.txt", "w")
        print("\nSaved " + saveName + ".txt to the current working directory.")
        for element in interestingList:
                resultsFile.write(element + "\n")
#       for element in emailList:
#               resultsFile.write(element + "\n")
        resultsFile.close()

#----CLEAN UP STEPS----

#Remove the temp directory, and its contents.
proc3 = subprocess.run(["rm","-r", "tempDir"])

#Remove the search results, if unwanted.
if saveResults == False:
        proc4 = subprocess.run(["rm", "search_results.txt"])
