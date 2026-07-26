#Open a file and read it then close the file

f = open("07_File_Input_&_Output/demo.txt","r")

data = f.read()

print(data)

f.close()