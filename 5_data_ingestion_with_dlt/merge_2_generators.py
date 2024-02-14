def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

# Merge the generators using the ID column
merged_people = {}

# Merge data from people_1
for person in people_1():
    merged_people[person["ID"]] = person

# Merge data from people_2
for person in people_2():
    if person["ID"] in merged_people:
        merged_people[person["ID"]].update(person)
    else:
        merged_people[person["ID"]] = person

# Calculate the sum of ages
total_age = sum(person["Age"] for person in merged_people.values())

# Print the merged data and total age
print("Merged People:")
for person in merged_people.values():
    print(person)

print("\nTotal age of all people:", total_age)
