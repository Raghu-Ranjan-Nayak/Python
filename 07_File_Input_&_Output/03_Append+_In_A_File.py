#Append the file and also read the file
f = open("07_File_Input_&_Output/demo.txt","a+")

f.write(" and then create a project")

print(f.read())

f.close()