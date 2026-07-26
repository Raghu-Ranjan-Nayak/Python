#Read file with syntax
with open("07_File_Input_&_Output/demo.txt","r") as f:
    data = f.read()

    print(data)

    #In with syntax do not want to close the file it atometicaly closed