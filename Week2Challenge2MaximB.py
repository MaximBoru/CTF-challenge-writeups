"""
Using a file that contains the entire English dictionary, Place the file in the same folder as your Python script.  
You will then need to create a script that counts how many words are in the dictionary that contain any consecutive 3-letter sequence in your firstname+lastname 

You are to ask the user for their full name (no spaces) and save that in the variable
"""

file = open('words.txt','r')
wordList = []
for lines in file:
   wordList.append(lines[:len(lines)])
file.close()

name = input("Enter your name with no spaces: ")
count = 0

for word in wordList:
    i = 0
    while i+3 <= len(word):
        if (word[i:i+3]).lower() not in name.lower():
            #print("fail", word[i:i+3])
            i += 1
        else:
            count += 1
            #print("success", word[i:i+3])
            break

print(f"There are {count} matches")
