#Vehicle Finder


#Function to List Cars
def vehicles():
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
  file = open("authorizedvehiclelist.txt", "r")
  response = file.read()
  print(response)
#Function to Search for a Car
def searchCar():
  car = input("Please Enter the full Vehicle Name: ")
  with open("authorizedvehiclelist.txt", 'r') as search:
    filing = search.read()
    if car in filing:
      print(str(car)+ " is an authorized vehicle")
    else:
      print(str(car)+ " is not an authorized vehicle")
#Function to Add Car
def addCar():
  newCar = input("Please Enter the full Vehicle name you would like to add: ")
  with open("authorizedvehiclelist.txt", "a") as file:
    file.write("\n")
    file.write(newCar)
    print("You have added " + str(newCar) + " as an authorized vehicle")

#Menu
while input != 5:
  print("********************************")
  print("AutoCountry Vehicle Finder v0.2")
  print("********************************")
  print("Please enter the following number below from the following menu:")
  print("1. PRINT all Authorized Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. Exit")

  menu = int(input(""))
  #Menu Selection
  if menu == 1:
    vehicles()

  if menu == 2:
    searchCar()

  if menu == 3:
    addCar()

  if menu == 4:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()
