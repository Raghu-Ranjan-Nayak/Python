#Some methods in dictionary
dict = {
    "name" : "Raghu",
    "cgpa" : 9.0,
    "marks" : [78,67,98]
}
#Get all keys
print(dict.keys())

#Get all vlaue
print(dict.values())

#Get all items
print(dict.items())

#Get vlaue of a perticular key
print(dict.get("marks"))

#Update the dict by new dict
new_dict = {"surname" : "Nayak",}
dict.update(new_dict)
print(dict)