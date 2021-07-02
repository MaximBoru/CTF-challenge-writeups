#MB

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