# #Write a programm which is create a practice.txt file and write something
# with open("07_File_Input_&_Output/Practice.txt","w") as f:


#     f.write("Hy everyone \ni am learning file i/o \nby using java. \n")
#     f.write("i like to learning programming by using java")

# #Write a rogramm which change the word java in to python
# with open("07_File_Input_&_Output/Practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("java","python")
# print(new_data)
    
# with open("07_File_Input_&_Output/Practice.txt","w") as f:
#     f.write(new_data)

#Write a programm which find the word learning in the paragraph or not
with open("07_File_Input_&_Output/Practice.txt","r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")

