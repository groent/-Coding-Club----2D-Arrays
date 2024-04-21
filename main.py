import csv
fields = ["First Name", "Last Name"]
hitList = [["Linus", "Torvalds"]]
def tablePrinter(list):
    for row in list:
        for item in row:
            print(item, end="\t")
        print(" ")
    #print(" ")



while True:
    #Add or Remove
    operation = input("Would you like to add or remove?\n> ")
    if operation.lower() == "add":
        name = input("Name?\n> ")
        laName = input("Last Name?\n> ")
        row = [name , laName]
        hitList.append(row)
    else:
        victim = input("Enter the Name of who you would like to remove:\n> ")
        for row in hitList:
            if victim in row:
                hitList.remove(row)

    
    exit = input("Exit? (y/N): ")
    if exit.lower() == "y":
        break
    else:
        continue
tablePrinter(hitList)

filename = input("How would you like to name your file?\n> ")

with open(f"{filename}.csv", 'a+') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(hitList)
    file.close()

with open(f"{filename}.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        print(row)
    file.close()