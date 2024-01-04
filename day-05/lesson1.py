# first loop class
cars = [
    "BMW",
    "Audi",
    "Porsche",
    "Wolkswagen"
]

# At this for sample, it will loop through all the itens of the list, until it ends
index = 0
for car in cars:
    print(f"The car is {car.upper()} and is's index is {index}")
    index += 1
