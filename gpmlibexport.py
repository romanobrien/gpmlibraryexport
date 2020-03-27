import os

compiled = open('compiled.csv','w')

# csv apostrophe encoding = &#39;
# csv ampersand encoding = &amp;
# csv quotation encoding = &quot;

def Encodecheck(titleOutput):
    # This function checks for any encoding of special characters in the song title, and replaces them with the correct character
    print(titleOutput)
    while "&#39;" in titleOutput or "&quot;" in titleOutput or "&amp;" in titleOutput:
        if "&#39;" in titleOutput:
            # Checks for encoding of apostrophes in song title and replaces with an actual apostrophe
            charnum = 0
            for character in titleOutput:
                if character == "&" and titleOutput[charnum+1] == "#":
                    titleOutput = titleOutput[0:charnum] + "\'" + titleOutput[charnum+5:]
                    charnum -=4
                charnum +=1

        if "&quot;" in titleOutput:
            # Checks for encoding of Quotation Marks
            charnum = 0
            for character in titleOutput:
                if character == "&" and titleOutput[charnum+1] == "q":
                    titleOutput = titleOutput[0:charnum] + "\"" + titleOutput[charnum+6:]
                    charnum -=5
                charnum +=1

        if "&amp;" in titleOutput:
            # Checks for encoding of Ampersands
            charnum = 0
            for character in titleOutput:
                if character == "&" and titleOutput[charnum+1] == "a":
                    titleOutput = titleOutput[0:charnum] + "&" + titleOutput[charnum+5:]
                    charnum -=4
                charnum +=1

    print(titleOutput)
    compiled.write(titleOutput + "\n")

for filename in os.listdir("Takeout/Google Play Music/Tracks"):
    # Finds each file in Tracks folder, then isolates the track name and artist name
    tracktitle = open("Takeout/Google Play Music/Tracks/"+filename, 'r')
    titleInput = tracktitle.read()
    stringmarks = []
    index = 0

    titleOutput = ""

    for character in titleInput:
        # This loops through the characters in the .csv file and adds each instance of " to index[]
        if character == "\"":
            stringmarks.append(index)
        index +=1

    for i in range(len(stringmarks)):
        # This loop grabs the text between each quoation mark in the csv and adds it to the string titleInput
        if i == 0:
            titleOutput += titleInput[stringmarks[i]+1:stringmarks[i+1]] + " - "
        elif i == 4:
            titleOutput += titleInput[stringmarks[i]+1:stringmarks[i+1]]

    Encodecheck(titleOutput)
    index = 0

compiled.close()
