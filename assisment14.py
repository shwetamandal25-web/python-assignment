import csv


with open("contacts.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Phone"])

    writer.writeheader()

    writer.writerow({"Name": "Shweta", "Phone": "9876543210"})
    writer.writerow({"Name": "Rahul", "Phone": "9876543211"})
    writer.writerow({"Name": "Riya", "Phone": "9876543212"})
    writer.writerow({"Name": "Aman", "Phone": "9876543213"})
    writer.writerow({"Name": "Neha", "Phone": "9876543214"})

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for contact in reader:
        if contact["Name"].startswith("R"):
            print(contact["Name"], contact["Phone"])