
import random
import math

class Pizzas():

   #SC1: Initializes the three variables alonside setting the price using the random module
   def __init__(self, MenuCode, MenuName, PizzaCount):
      self.MenuCode = MenuCode
      self.MenuName = MenuName
      self.PizzaCount = PizzaCount
      #SC2: Sets the price of the pizza using the random module
      self.MenuPrice = random.randint(10, 20)


   #SC3: returns Total Inventory Cost
   def getValue(self):
     TotalInventoryCost = self.PizzaCount * self.MenuPrice
     return TotalInventoryCost

  #SC4: Returns final output with correct object attributes
   def toString(self):
     print("Menu Code:", self.MenuCode) 
     print("Menu Name:", self.MenuName)
     #SC5: prints out the price of the pizza and total inventory cost in USD format
     print("Menu Price: $" + str(self.MenuPrice) + ".00")
     print("Total Pizza Count:", self.PizzaCount)
     print("Total Inventory Cost: $" + str(self.getValue()) + ".00")
    

########################
########################
#DRIVER SECTION

#The Function where the main code is executed, mainly used for organization
def main():

  cont = 1
  while cont == 1:

    #SC6: catches if user enters a non-integer value, reiterating through the loop if so
    try:
      PizzaItems = int(input("\nHow many simulated frozen pizzas do you want to create? You must enter a number between 1 and 10.\n"))
    except ValueError:
      print("WARNING! You cannot enter in letters. try again")
      continue

    #SC7: catches if user enters a number less than 1 or greater than 10, reiterating through the loop if so
    if PizzaItems < 1 or PizzaItems > 10:
       print("WARNING! You entered a value that was out of range. try again")
       continue
    else:
      print("You entered: " + str(PizzaItems))
      cont = 0


  print("\nYou will now create the menu item code for the inventory management system, name of the menu item, and how much inventory for the pizza to keep in the freezer. The price will be randomly generated.")

  PizzaList = []
  for i in range(PizzaItems):
   
    cont = 1
    while cont == 1:

      MenuCode = input("\nPlease enter a three letter/number menu code for pizza " + str(i+1) + ":\n")

      #SC8: makes sure the code is exactly 3 digits/letters long, reiterating through the loop if not
      if len(MenuCode) != 3:
        print("WARNING! You entered an incorrect value. try again")
        continue
      else:
        print("You entered: " + MenuCode)
        cont = 0

    #SC9: code to enter pizza name
    MenuName = input("\nPlease enter the pizza name:\n")

    cont = 1
    while cont == 1:

      #SC10: catches if user enters a non-integer value, reiterating through the loop if so
      try:
        PizzaCount = int(input("\nPlease enter total inventory count for this " + MenuName + " pizza to keep in the freezer:\n"))
      except ValueError:
        print("WARNING! You cannot enter in letters. try again")
        continue

      cont = 0

    #SC11: creates a new object using the Pizzas class and stores into a list called PizzaList
    PizzaList.append(Pizzas(MenuCode, MenuName, PizzaCount))

  
  
  print("\nListed below is your current pizza inventory:")

  #SC12: prints out all pizza objects from list
  for pizza in PizzaList:
    pizza.toString()
    print("\n")
    
    


                       
    

    
  
      


main()
