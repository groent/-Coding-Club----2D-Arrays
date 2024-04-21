#Tell Python that you are using .csv Files
import csv
#The fields that will go at the top of the table
fields = ["First Name", "Last Name"]
#Place Holder name
hitList = [["Theodore", "Groen"]]

#2D Array Printer
def tablePrinter(list):
    #Cycle through rows of the list
    for row in list:
        #Cycle through Items of each Row
        for item in row:
            #Print the Items of Each Row
            print(item, end="\t")
        #Add Separation
        print(" ")



#initiate program
while True:
    #Ask if the user wants to add or remove
    operation = input("Would you like to add or remove?\n> ")
    if operation.lower() == "add":
        name = input("Name?\n> ")
        laName = input("Last Name?\n> ")
        #Append a Row with the first element being name, and second Last Name
        row = [name , laName]
        hitList.append(row)
    #Remove Row
    else:
        #Name to remove
        victim = input("Enter the Name of who you would like to remove:\n> ")
        #Look for who to remove
        for row in hitList:
            #If the victim is found remove ENTIRE ROW, else there will be weird floating data
            if victim in row:
                hitList.remove(row)

    #Exit button
    exit = input("Exit? (y/N): ")
    #Use .lower() to avoid problems with CAPS
    if exit.lower() == "y":
        break
    else:
        continue
#Indented outside While Loop, prints the entire list
tablePrinter(hitList)
#Get file name
filename = input("How would you like to name your file?\n> ")

#Open a new csv file with previously assigned name "a+" means read, write, append
with open(f"{filename}.csv", 'a+') as file:
    #Assign the writer
    csvwriter = csv.writer(file)
    #Write the "fields" row in the beggning
    csvwriter.writerow(fields)
    #Write every single row we have added
    csvwriter.writerows(hitList)
    #Close the file for safety
    file.close()

#Open file "r" means read-only, This is for debugging purposes.
with open(f"{filename}.csv", 'r') as file:
    #Assign a reader
    csvreader = csv.DictReader(file)
    #For each row in the file print in console
    for row in csvreader:
        print(row)
    #close the file
    file.close()