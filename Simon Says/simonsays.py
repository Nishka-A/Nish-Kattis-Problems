#Get information from the console and put it into lines
lines = raw_input()

#Loop through each line until you hit the end of lines
for i in range(int(lines)):
    line1 = raw_input()
    #If the line starts with "Simon says ", splice and print it
    if line1.startswith("Simon says "):
        print(line1[11:])
