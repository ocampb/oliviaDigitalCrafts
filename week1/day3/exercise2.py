# Remove all empty strings in this list
from os import remove


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# output ["Mike", "Emma", "Kelly", "Brad"]

for list in list1:
    if list == "": list1.remove(list)

print(list1)