def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

# Sum ages from both generators
total_age = 0

# Sum ages from people_1
for person in people_1():
    total_age += person["Age"]

# Sum ages from people_2
for person in people_2():
    total_age += person["Age"]

# Print the total age
print("Total age from both generators:", total_age)
