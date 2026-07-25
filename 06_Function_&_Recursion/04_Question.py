#Write a recursive function to print all elements of a list
def print_el(list,ind = 0):
    if(ind == len(list)):
        return
    else:
        print(list[ind])
        print_el(list,ind + 1)

name = ["Raghu","Raja","Akshay"]
print_el(name)