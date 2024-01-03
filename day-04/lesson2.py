# A list is a data structure
# In Lists, the order is not lost.

cars = [
    "BMW",
    "Ferrari",
    "Alfa Romeo"
]

# Adding a new item to the end of the list
# The append method adds a single item to the END of the list
cars.append("Ford") 

print(cars)

# The extend method accepts a list with items to be added to the end of the original list.
cars.extend(["Mercedez", "Porsche", "Audi"])
print(cars)
