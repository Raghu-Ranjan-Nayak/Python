#Creating a nested dictionary
student = {
    "name" : "Raghu",
    "cgpa" : 9.0,
    "subjects" : {
        "phy" : 96,
        "che" : 98,
        "math" : 100
    }
}
student["surname"] = "Nayak"
print(student["subjects"]["math"])
print(student)