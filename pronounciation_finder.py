import csv 
import requests
from bs4 import BeautifulSoup
import re

print("Welcome to Pronounciation Finder")
print("This project uses the Merriam Webster Dictionary to find pronounciations of words in the English language.")

againAnswer = "Y"
word = ""
exiting = False

while againAnswer == "Y" or againAnswer == "y":
    isAWord = False
    while not isAWord:
        print("Enter your word: (Q: quit)")

        word = input()
        if word == "Q" or word == "q":
            exiting = True
            break        
        response = requests.get("https://www.merriam-webster.com/dictionary/" + word)
        if response.status_code == 200:
            isAWord = True
        else:
            print("Please input an English word")
    if exiting:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all("span", class_ = "pr")
    prs = set(())
    for t in tags:
        prs.add(t.text.strip())
    
    toPrint = len(prs)
    for pr in prs:
        if toPrint > 1:
            print(pr, end = ', ')
        else:
            print(pr)
        toPrint -= 1
    print("Would you like to find the pronounciation of another word? (Y/N)")
    againAnswer = input()
    
print("Thank you for using Pronounciation Finder")
